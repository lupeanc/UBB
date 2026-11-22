
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <iomanip>
#include <algorithm>
#include <mpi.h>

using namespace std;

// TEST DEADLOCK HERE - the normal test is done without it, but just for corectness sake
 //#define USE_MPI_SSEND
// MPI vs Threads: Threads - multiple in the same process, MPI - multiple processes, each with its own memory space. Threads share memory, MPI processes do not.

// ifdef -> to check whether there is a preprocessor already defined
// if yes (^ is NOT commented): SEND becomes MPI_Ssend - syncronous send, the sender will wait until the receiver has received the message
// if not (^ is commented): SEND becomes MPI_Send - asyncronous send, the sender will not wait for the receiver to receive the message
#ifdef USE_MPI_SSEND
#define SEND MPI_Ssend
#else
#define SEND MPI_Send
#endif

#define NUMBER_1_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar1.txt"
#define NUMBER_2_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar2.txt"
#define OUTPUT_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar3.txt"
#define SEQUENTIAL_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Sequential.txt"

// Tags for MPI messages - basically IDs for the different types of messages
const int TAG_NUMBER1 = 1;
const int TAG_NUMBER2 = 2;
const int TAG_CARRY = 3;
const int TAG_RESULT = 4;

// Reads the next digit, ignoring whitespace.
bool readDigit(ifstream& file, uint8_t& digit) {
    char c;

    // >> reads next character, skipping whitespaces
	// if the read fails, return false
    if (!(file >> c))
        return false;

	// if the character is not a digit, return false
    if (c < '0' || c > '9')
        return false;

	// Convert the character to a digit (0-9).
    digit = static_cast<uint8_t>(c - '0');
    return true;
}

// Calculates how many digits a worker receives.
//  N = total number of digits, 
// workers = total number of workers, 
// rank = rank (ID) of the current worker
int getChunkSize(int N, int workers, int rank) {
    int base = N / workers;
    int remainder = N % workers;

    // base  = how many digits each worker gets by default
    // if the remainder is > than the current id of the worker
    // then the worker gets 1 extra digit
    // RANK - 1 BECAUSE RANK 0 IS ONLY USED TO READING/RECEIVING VALUES, NO COMPUTING
    return base + (rank - 1 < remainder ? 1 : 0);
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

	// Initialize the MPI environment with main args
    MPI_Init(&argc, &argv);

    // id and number of threads
    // p is gotten by -n <p> in the script
    int rank, p;

	// MPI_COMM_WORLD = communicator containing all processes.
    // get the id of the current process and store it in rank
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // get the total number of processes and stores it in p
    MPI_Comm_size(MPI_COMM_WORLD, &p);

    // number 1 number of digits, number 2 ..., maximum number of digits from N1 and N2
    int N1 = 0, N2 = 0, N = 0;

    // proc 0 reads the numbers
    // for every process, it sends the corresponding digits to be taken care of
    if (rank == 0) {

        // opens the input files.
        ifstream file1(NUMBER_1_FILE);
        ifstream file2(NUMBER_2_FILE);

        if (!file1 || !file2) {
            cerr << "Could not open input files.\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        // Read the number of digits from each file.
        if (!(file1 >> N1) || !(file2 >> N2) ||
            N1 <= 0 || N2 <= 0) {

            cerr << "Invalid input file headers.\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        N = max(N1, N2);

        // Bcast - Share the input sizes with all processes.
        // address of variable being sent
        // number of elems
        // data type
        // rank of the process sending the info
        // communicator
        MPI_Bcast(&N1, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Bcast(&N2, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Bcast(&N, 1, MPI_INT, 0, MPI_COMM_WORLD);

        int workers = p - 1;

        // Distribute the digits incrementally.
        for (int destinationProcess = 1; destinationProcess < p; destinationProcess++) {

            int count = getChunkSize(N, workers, destinationProcess);

            // initialize the vectors with 0 
            vector<uint8_t> digits1(count, 0);
            vector<uint8_t> digits2(count, 0);

            // go through the digits
            for (int i = 0; i < count; i++) {

                // original position of the digits is basically:
                // default number of digits * how many workers until now
                // + MIN(how many workers until now, how many left over digits)
                // + select the current digit within worker's chunk
                // ex: N = 18, workers = 4
                // => W1: position = (1-1) * 4 + min(1 - 1, 2) + currentDigit
                // => W3: position = (3 - 1) * 4 + min(3 - 1, 2) + currentDigit
                int position =
                    (destinationProcess - 1) * (N / workers)
                    + min(destinationProcess - 1, N % workers) + i;

                // Read only the digits that actually exist.
                if (position < N1) {
                    // read digit and put it in vector 1
                    if (!readDigit(file1, digits1[i])) {
                        cerr << "Invalid digits in Numar1.txt\n";
                        MPI_Abort(MPI_COMM_WORLD, 1);
                    }
                }

                if (position < N2) {
                    // read digit and put it in vector 2
                    if (!readDigit(file2, digits2[i])) {
                        cerr << "Invalid digits in Numar2.txt\n";
                        MPI_Abort(MPI_COMM_WORLD, 1);
                    }
                }
            }

            // Send the first and second number's digit chunks.
            // digits1.data() -> pointer to the first element of the vector
            // numer of digits being sent
            // data type
            // destination process id
            // message identifier
            // communicator
            SEND(digits1.data(), count, MPI_UNSIGNED_CHAR,
                destinationProcess, TAG_NUMBER1, MPI_COMM_WORLD);

            SEND(digits2.data(), count, MPI_UNSIGNED_CHAR,
                destinationProcess, TAG_NUMBER2, MPI_COMM_WORLD);
        }

        file1.close();
        file2.close();

        // Open the output file.
        ofstream output(OUTPUT_FILE);

        if (!output) {
            cerr << "Could not create Numar3.txt\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        int resultLength = 0;

        // Receive the result chunks in digit order.
        for (int source = 1; source < p; source++) {

            int count = getChunkSize(N, workers, source);

            int receiveCount = count;

            // the final worker needs an extra count for its carry
            if (source == p - 1)
                receiveCount++;

            vector<uint8_t> result(receiveCount);

            // receive the result from the current woker
            MPI_Recv(result.data(), receiveCount,
                MPI_UNSIGNED_CHAR, source, TAG_RESULT,
                MPI_COMM_WORLD, MPI_STATUS_IGNORE);

            // Write the received digits immediately.
            for (int i = 0; i < count; i++) {
                output.put('0' + result[i]);
                resultLength++;
            }

            // The last worker's additional digit is the final carry.
            if (source == p - 1 && result[count] != 0) {
                output.put('0' + result[count]);
                resultLength++;
            }
        }
    
        output << resultLength << '\n';

        output.close();
    }

    else {

        int workers = p - 1;
        int count;

        // Receive the sizes of the original numbers.
        MPI_Bcast(&N1, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Bcast(&N2, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Bcast(&N, 1, MPI_INT, 0, MPI_COMM_WORLD);

        count = getChunkSize(N, workers, rank);

        // Receive the two digit chunks FIRST.
        vector<uint8_t> digits1(count);
        vector<uint8_t> digits2(count);

        MPI_Recv(digits1.data(), count, MPI_UNSIGNED_CHAR,
            0, TAG_NUMBER1, MPI_COMM_WORLD,
            MPI_STATUS_IGNORE);

        MPI_Recv(digits2.data(), count, MPI_UNSIGNED_CHAR,
            0, TAG_NUMBER2, MPI_COMM_WORLD,
            MPI_STATUS_IGNORE);

        // Receive the carry from the previous process.
        // Process 1 starts with carry = 0.
        int carry = 0;

        if (rank > 1) {
            MPI_Recv(&carry, 1, MPI_INT,
                rank - 1, TAG_CARRY,
                MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        }

        // Add the digits belonging to this process.
        vector<uint8_t> result(count);

        for (int i = 0; i < count; i++) {

            int currentDigitSum =
                digits1[i] + digits2[i] + carry;

            result[i] = currentDigitSum % 10;
            carry = currentDigitSum / 10;
        }

        // Send the carry to the next process.
        if (rank < p - 1) {
            SEND(&carry, 1, MPI_INT,
                rank + 1, TAG_CARRY, MPI_COMM_WORLD);
        }

        // The last process must preserve the final carry.
        if (rank == p - 1) {
            result.push_back(static_cast<uint8_t>(carry));
        }

        // Send the calculated result to process 0.
        SEND(result.data(), static_cast<int>(result.size()),
            MPI_UNSIGNED_CHAR, 0, TAG_RESULT, MPI_COMM_WORLD);
    }

    MPI_Finalize();

    checkResults(SEQUENTIAL_FILE, OUTPUT_FILE);

    return 0;
}
