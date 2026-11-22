
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <iomanip>
#include <algorithm>
#include <mpi.h>

using namespace std;

// V2 = scatter + gather -> proc 0 also participates in additon

#define NUMBER_1_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar1.txt"
#define NUMBER_2_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar2.txt"
#define OUTPUT_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar3.txt"
#define SEQUENTIAL_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Sequential.txt"

const int TAG_CARRY = 1;

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

    // Remove extra 0's at the end of the result
    while (resultLength > 1 && result[resultLength - 1] == 0) {
        resultLength--;
    }

    ofstream output(OUTPUT_FILE);

    if (!output) {
        cerr << "Could not create Numar3.txt\n";
        return;
    }

    // Write the number of result digits in the header
    output << resultLength << '\n';

    // Digits are stored from least significant to most significant.
    // Write them in reverse order.
    for (int i = resultLength - 1; i >= 0; i--) {
        output.put('0' + result[i]);
    }

    output << '\n';
    output.close();
}

string removeLeadingZeros(string number) {
    size_t pos = number.find_first_not_of('0');

    // string::npos = no matching position was found
    if (pos == string::npos)
        return "0";

	// return the substring starting from the first non-zero character
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

    // 1. Init MPI
    MPI_Init(&argc, &argv);

    int rank, p;

	// 2. Get rank and size
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &p);

    int N1 = 0, N2 = 0;
    int N = 0;
    int chunkSize = 0;

    vector<uint8_t> digits1;
    vector<uint8_t> digits2;

    // PROCESS 0: READ BOTH NUMBERS
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

        // Increase N until it is divisible by p so we can 
		// distribute the digits equally among all processes
        while (N % p != 0) {
            N++;
        }

        chunkSize = N / p;

        // Initialize both arrays with zeros.
        digits1.resize(N, 0);
        digits2.resize(N, 0);

        // Read the first number.
        for (int i = 0; i < N1; i++) {
            if (!readDigit(file1, digits1[i])) {
                cerr << "Invalid digits in Numar1.txt\n";
                MPI_Abort(MPI_COMM_WORLD, 1);
            }
        }

        // Read the second number.
        for (int i = 0; i < N2; i++) {
            if (!readDigit(file2, digits2[i])) {
                cerr << "Invalid digits in Numar2.txt\n";
                MPI_Abort(MPI_COMM_WORLD, 1);
            }
        }

        file1.close();
        file2.close();
    }

    // Share the chunk size with all processes.
    MPI_Bcast(&chunkSize, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // local vectors for the chunks of digits to be used
    vector<uint8_t> local1(chunkSize);
    vector<uint8_t> local2(chunkSize);

    // Distribute the first number
    // with MPI scatter: takes data from one process
	// and distributes it to all processes, including itself
    // so, process 0 will send digits1 data, the number of elements to send, and the type
	// all other processes will receive the data into their local1 vector
	// 0 is the sender, so all the other wait for the data to be sent
	// CONDITIONAL: used bc only process 0 has the data to send, all others have nullptr
    // ALSO BECAUSE SCATTER NEEDS TO BE CALLED BY ALL PROCESSES
    MPI_Scatter(
        rank == 0 ? digits1.data() : nullptr,
        chunkSize,
        MPI_UNSIGNED_CHAR,
        local1.data(),
        chunkSize,
        MPI_UNSIGNED_CHAR,
        0,
        MPI_COMM_WORLD
    );

    // Distribute the second number.
    MPI_Scatter(
        rank == 0 ? digits2.data() : nullptr,
        chunkSize,
        MPI_UNSIGNED_CHAR,
        local2.data(),
        chunkSize,
        MPI_UNSIGNED_CHAR,
        0,
        MPI_COMM_WORLD
    );

    // Each process calculates its own result chunk
    vector<uint8_t> localResult(chunkSize);

    int carry = 0;

    // Process 0 starts with carry = 0
    // Other processes receive the carry from the previous process
    if (rank > 0) {
        MPI_Recv(
            &carry,
            1,
            MPI_INT,
            rank - 1,
            TAG_CARRY,
            MPI_COMM_WORLD,
            MPI_STATUS_IGNORE
        );
    }

    // Add the digits
    for (int i = 0; i < chunkSize; i++) {

        int currentDigitSum = local1[i] + local2[i] + carry;

        localResult[i] = currentDigitSum % 10;
        carry = currentDigitSum / 10;
    }

    // Send the carry to the next process
    if (rank < p - 1) {
        MPI_Send(
            &carry,
            1,
            MPI_INT,
            rank + 1,
            TAG_CARRY,
            MPI_COMM_WORLD
        );
    }

    // Gather all result chunks at process 0
    vector<uint8_t> finalResult;

	// Allocate space for the final result in process 0
	// chunkSize * p is the total number of digits, plus 1 for the final carry
    if (rank == 0) {
        finalResult.resize(chunkSize * p + 1);
    }

    // opposite of scatter:
	// gathers all the local results from each process into the finalResult vector in process 0
	// ONLY process 0 will receive the data => rank == 0 ? finalResult.data() : nullptr
	// 0 is the root process that will gather the data
    MPI_Gather(
        localResult.data(),
        chunkSize,
        MPI_UNSIGNED_CHAR,
        rank == 0 ? finalResult.data() : nullptr,
        chunkSize,
        MPI_UNSIGNED_CHAR,
        0,
        MPI_COMM_WORLD
    );

	// Get the final carry from the last process and send it to process 0
    if (rank == p - 1) {
        MPI_Send(
			&carry,
            1,
            MPI_INT,
			0,
			TAG_CARRY,
			MPI_COMM_WORLD
        );
    }

    // PROCESS 0: COMPLETE AND WRITE THE RESULT.
    if (rank == 0) {
		int finalCarry = 0;

        MPI_Recv(
            &finalCarry,
            1,
            MPI_INT,
            p - 1,
            TAG_CARRY,
            MPI_COMM_WORLD,
            MPI_STATUS_IGNORE
        );

        // The last process has the final carry.
        finalResult[chunkSize * p] = finalCarry;

        writeResult(finalResult);

        cout << "Variant 2 finished successfully.\n";
    }

    MPI_Finalize();

	checkResults(SEQUENTIAL_FILE, OUTPUT_FILE);

    return 0;
}
