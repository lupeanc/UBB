#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <iomanip>
#include <algorithm>
#include <mpi.h>

using namespace std;

// basically V1, but instead of reading the whole numbers
// we read a chunk at once and send it to the current worker ASYNCHRONOUSLY
// => Its best to have N divisible by p-1 (number of workers)
#define NUMBER_1_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar1.txt"
#define NUMBER_2_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar2.txt"
#define OUTPUT_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar3.txt"
#define SEQUENTIAL_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Sequential.txt"

const int TAG_NUMBER1 = 1;
const int TAG_NUMBER2 = 2;
const int TAG_CARRY = 3;
const int TAG_RESULT = 4;

// Reads one digit, ignoring whitespace.
bool readDigit(ifstream& file, uint8_t& digit) {
    char c;

    if (!(file >> c))
        return false;

    if (c < '0' || c > '9')
        return false;

    digit = static_cast<uint8_t>(c - '0');
    return true;
}

// Writes the result in normal order.
void writeResult(const vector<uint8_t>& result) {

    int resultLength = static_cast<int>(result.size());

    // Remove unnecessary leading zeros.
    while (resultLength > 1 && result[resultLength - 1] == 0) {
        resultLength--;
    }

    ofstream output(OUTPUT_FILE);

    if (!output) {
        cerr << "Could not create Numar3.txt\n";
        return;
    }

    output << setw(10) << setfill('0') << resultLength << '\n';

    // Write from most significant digit to least significant digit.
    for (int i = resultLength - 1; i >= 0; i--) {
        output.put('0' + result[i]);
    }

    output << '\n';
    output.close();
}

string removeLeadingZeros(string number) {
    size_t pos = number.find_first_not_of('0');

    if (pos == string::npos)
        return "0";

    return number.substr(pos);
}

bool checkResults(const string& sequentialFile, const string& mpiFile) {

    ifstream file1(sequentialFile);
    ifstream file2(mpiFile);

    if (!file1 || !file2) {
        cerr << "Could not open result files.\n";
        return false;
    }

    string sequentialResult;
    string mpiHeader;
    string mpiResult;

    file1 >> sequentialResult;

    // Skip the MPI output header.
    file2 >> mpiHeader;

    // Read the actual MPI result.
    file2 >> mpiResult;

    sequentialResult = removeLeadingZeros(sequentialResult);
    mpiResult = removeLeadingZeros(mpiResult);

    if (sequentialResult == mpiResult) {
        return true;
    }

    cout << "Results do not match!\n";
    cout << "Sequential: " << sequentialResult << '\n';
    cout << "MPI:        " << mpiResult << '\n';

    return false;
}

int main(int argc, char** argv) {

    // mpi init
    MPI_Init(&argc, &argv);

    int rank, p;

    // get rank and size
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &p);

    int N1 = 0, N2 = 0;
    int N = 0;
    int totalWorkers = p - 1;
    int chunkSize = 0;

	// 0: reads the numbers and distributes them to the workers
    // CHUNK BY CHUNK
    if (rank == 0) {

        ifstream file1(NUMBER_1_FILE);
        ifstream file2(NUMBER_2_FILE);

        if (!file1 || !file2) {
            cerr << "Could not open input files.\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        // Read the number of digits.
        if (!(file1 >> N1) || !(file2 >> N2) ||
            N1 <= 0 || N2 <= 0) {

            cerr << "Invalid input file headers.\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        N = max(N1, N2);

        // Divide the digits among the p - 1 workers.
        // Increase N until it is divisible by the number of workers.
        while (N % totalWorkers != 0) {
            N++;
        }

        chunkSize = N / totalWorkers;

        // Tell the workers how many digits they will receive
        // stuff's basically saying that we updated the variable chunkSize
        MPI_Bcast(&chunkSize, 1, MPI_INT, 0, MPI_COMM_WORLD);

        // Process 0 sends ONE CHUNK AT A TIME
        int idCurrentProcess = 1;

        while (idCurrentProcess <= totalWorkers) {

            vector<uint8_t> digits1(chunkSize, 0);
            vector<uint8_t> digits2(chunkSize, 0);

            // Read the current chunk
            for (int i = 0; i < chunkSize; i++) {

                int position =
                    (idCurrentProcess - 1) * chunkSize + i;

                if (position < N1) {
                    if (!readDigit(file1, digits1[i])) {
                        cerr << "Invalid digits in Numar1.txt\n";
                        MPI_Abort(MPI_COMM_WORLD, 1);
                    }
                }

                if (position < N2) {
                    if (!readDigit(file2, digits2[i])) {
                        cerr << "Invalid digits in Numar2.txt\n";
                        MPI_Abort(MPI_COMM_WORLD, 1);
                    }
                }
            }

			// Send both chunks ASYNCHRONOUSLY to the current worker
            // the request thing is just MPI's way of handling async communication
            MPI_Request sendRequests[2];

            MPI_Isend(
                digits1.data(),
                chunkSize,
                MPI_UNSIGNED_CHAR,
                idCurrentProcess,
                TAG_NUMBER1,
                MPI_COMM_WORLD,
                &sendRequests[0]
            );

            MPI_Isend(
                digits2.data(),
                chunkSize,
                MPI_UNSIGNED_CHAR,
                idCurrentProcess,
                TAG_NUMBER2,
                MPI_COMM_WORLD,
                &sendRequests[1]
            );

            // Wait for sends to finish so we dont
            // wipe the vectors from existence before that :)))
            MPI_Waitall(2, sendRequests, MPI_STATUSES_IGNORE);
			//MPI_Wait(&sendRequests[0], MPI_STATUS_IGNORE);

            idCurrentProcess++;
        }

        file1.close();
        file2.close();

        // Receive the results asynchronously.
        vector<vector<uint8_t>> partialResults(
            totalWorkers,
            vector<uint8_t>(chunkSize + 1, 0)
        );

        vector<MPI_Request> receiveRequests(totalWorkers);

        for (int worker = 1; worker <= totalWorkers; worker++) {

            MPI_Irecv(
                partialResults[worker - 1].data(),
                chunkSize + 1,
                MPI_UNSIGNED_CHAR,
                worker,
                TAG_RESULT,
                MPI_COMM_WORLD,
                &receiveRequests[worker - 1]
            );
        }

        // Wait until all results have arrived.
        MPI_Waitall(
            totalWorkers,
            receiveRequests.data(),
            MPI_STATUSES_IGNORE
        );

        // Combine the chunks in digit order.
        vector<uint8_t> finalResult(N + 1, 0);

        for (int worker = 0; worker < totalWorkers; worker++) {

            for (int i = 0; i < chunkSize; i++) {

                int position = worker * chunkSize + i;

                finalResult[position] =
                    partialResults[worker][i];
            }
        }

        // The last worker provides the final carry.
        finalResult[N] = partialResults[totalWorkers - 1][chunkSize];

        writeResult(finalResult);

    }

    // WORKERS: RECEIVE, ADD AND SEND RESULTS.
    else {

        // Receive the chunk size.
        MPI_Bcast(&chunkSize, 1, MPI_INT, 0, MPI_COMM_WORLD);

        vector<uint8_t> digits1(chunkSize);
        vector<uint8_t> digits2(chunkSize);

        int carry = 0;

        MPI_Request receiveRequests[3];

        // Receive both digit chunks from process 0.
        MPI_Irecv(
            digits1.data(),
            chunkSize,
            MPI_UNSIGNED_CHAR,
            0,
            TAG_NUMBER1,
            MPI_COMM_WORLD,
            &receiveRequests[0]
        );

        MPI_Irecv(
            digits2.data(),
            chunkSize,
            MPI_UNSIGNED_CHAR,
            0,
            TAG_NUMBER2,
            MPI_COMM_WORLD,
            &receiveRequests[1]
        );

        // Processes with rank > 1 also receive a carry.
        if (rank > 1) {

            MPI_Irecv(
                &carry,
                1,
                MPI_INT,
                rank - 1,
                TAG_CARRY,
                MPI_COMM_WORLD,
                &receiveRequests[2]
            );

            // Wait for both digits and carry.
            MPI_Waitall(
                3,
                receiveRequests,
                MPI_STATUSES_IGNORE
            );
        }
        else {

            // Worker 1 starts with carry = 0.
            MPI_Waitall(
                2,
                receiveRequests,
                MPI_STATUSES_IGNORE
            );
        }

        // Add the received digits.
        vector<uint8_t> result(chunkSize + 1, 0);

        for (int i = 0; i < chunkSize; i++) {

            int currentDigitSum =
                digits1[i] + digits2[i] + carry;

            result[i] = currentDigitSum % 10;
            carry = currentDigitSum / 10;
        }

        // Send the carry to the next worker asynchronously.
        MPI_Request carryRequest;

        if (rank < p - 1) {

            MPI_Isend(
                &carry,
                1,
                MPI_INT,
                rank + 1,
                TAG_CARRY,
                MPI_COMM_WORLD,
                &carryRequest
            );

            MPI_Wait(&carryRequest, MPI_STATUS_IGNORE);
        }

        // Only the last worker needs to preserve the final carry.
        if (rank == p - 1) {
            result[chunkSize] = static_cast<uint8_t>(carry);
        }

        // Send the result to process 0 asynchronously.
        MPI_Request resultRequest;

        MPI_Isend(
            result.data(),
            chunkSize + 1,
            MPI_UNSIGNED_CHAR,
            0,
            TAG_RESULT,
            MPI_COMM_WORLD,
            &resultRequest
        );

        MPI_Wait(&resultRequest, MPI_STATUS_IGNORE);
    }

    MPI_Finalize();

	checkResults(SEQUENTIAL_FILE, OUTPUT_FILE);

    return 0;
}
