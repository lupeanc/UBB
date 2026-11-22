#include <iostream>
#include <fstream>
#include <cstdint>
#include <vector>
using namespace std;

#define NUMBER_1_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar1.txt"
#define NUMBER_2_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar2.txt"
#define OUTPUT_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Sequential.txt"

void sequential(uint8_t n1[], uint8_t n2[], uint8_t result[], int size) {
    int carry = 0;

    for (int i = 0; i < size; i++) {
        int currentDigitSum = n1[i] + n2[i] + carry;

        result[i] = currentDigitSum % 10;
        carry = currentDigitSum / 10;
    }

    result[size] = carry;
}

int main()
{
	int N1, N2, N;
    ifstream file1(NUMBER_1_FILE);
    ifstream file2(NUMBER_2_FILE);

    if (!file1 || !file2) {
        cerr << "Could not open input files.\n";
        return 1;
    }

    // Read the number of digits from each file.
    if (!(file1 >> N1) || !(file2 >> N2) ||
        N1 <= 0 || N2 <= 0) {

        cerr << "Invalid input file headers.\n";
		return 1;
    }

    N = max(N1, N2);

    vector<uint8_t> digits1(N, 0);
    vector<uint8_t> digits2(N, 0);
    vector<uint8_t> result(N + 1, 0);

    for (int i = 0; i < N1; i++) {
        char digit;
        file1 >> digit;
        digits1[i] = digit - '0';
    }

    for (int i = 0; i < N2; i++) {
        char digit;
        file2 >> digit;
        digits2[i] = digit - '0';
    }

    sequential(digits1.data(), digits2.data(), result.data(), N);

	ofstream outputFile(OUTPUT_FILE);

    for (int i = N; i >= 0; i--) {
        if (i == N && result[i] == 0) {
            continue;
        }

        outputFile << static_cast<int>(result[i]);
    }

    return 0;
}