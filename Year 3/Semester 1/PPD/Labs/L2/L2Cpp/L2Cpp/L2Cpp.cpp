#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <math.h>
#include <chrono>
#include <thread>
#include <mutex>

using namespace std;
using namespace chrono;

#define MAX 10000
#define CONV_MAX 3

//int f[MAX][MAX];
//int c[CONV_MAX][CONV_MAX];
vector<vector<double>> f;
vector<vector<double>> c;

#define matrixFFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\MatrixF.txt"
#define convMatrixFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\ConvolutionM.txt"
#define outputFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\output.txt"
#define sequentialOutputFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L2\\L2Cpp\\L2Cpp\\sequentialOutput.txt"

void readMatrices() {
	f.clear();
	c.clear();

	ifstream matrixFFile(matrixFFilePath);
	ifstream convMatrixFile(convMatrixFilePath);

	string line;

	// read matrix F
	if (matrixFFile.is_open()) {
		while (getline(matrixFFile, line)) {
			if (line.empty()) {
				continue; // Skip empty lines
			}

			stringstream lineStream(line);
			vector<double> values;
			string value;

			while (lineStream >> value) {
				values.push_back(stod(value.c_str()));
			}

			if (!values.empty()) {
				f.push_back(values);
			}
		}

		//for (int i = 0; i < matrixF.size() && i < MAX; i++) {
		//	for (int j = 0; j < matrixF[i].size() && j < MAX; j++) {
		//		f[i][j] = matrixF[i][j];
		//	}
		//}
	}
	else {
		cout << "Unable to open file: " << matrixFFilePath << endl;
	}

	// read convolution matrix
	if (convMatrixFile.is_open()) {
		while (getline(convMatrixFile, line)) {
			if (line.empty()) {
				continue; // Skip empty lines
			}

			stringstream lineStream(line);
			vector<double> values;
			string value;

			while (lineStream >> value) {
				values.push_back(stod(value.c_str()));
			}

			if (!values.empty()) {
				c.push_back(values);
			}

		}

		//for (int i = 0; i < convMatrix.size() && i < CONV_MAX; i++) {
		//	for (int j = 0; j < convMatrix[i].size() && j < CONV_MAX; j++) {
		//		c[i][j] = convMatrix[i][j];
		//	}
		//}

	}
	else {
		cout << "Unable to open file: " << convMatrixFilePath << endl;
	}
}

void writeMatrix(vector<vector<double>>& matrix, int n, int m, string filePath) {
	ofstream outputFile(filePath);
	if (outputFile.is_open()) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				outputFile << matrix[i][j] << " ";
			}
			outputFile << endl;
		}
		outputFile.close();
	}
	else {
		cout << "Unable to open file: " << outputFilePath << endl;
	}
}

bool validate(int n, int m) {
	ifstream expectedValues(sequentialOutputFilePath);
	string line;
	int ni=0, mj=0;

	if (expectedValues.is_open()) {
		while (getline(expectedValues, line)) {
			if (line.empty()) {
				continue; // Skip empty lines
			}

			stringstream lineStream(line);
			string value;
			int intValue;

			while (lineStream >> value) {
				intValue = stod(value.c_str());

				if (intValue != f[ni][mj]) {
					return false;
				}

				// if we get to the end of the row
				if (mj + 1 == m) {
					mj = 0;
					ni++;
				}
				else {
					mj++;
				}
			}
		}

	}
	
	return true;
}

int calculateCell(int j, int m, vector<double>& previousRow, vector<double>& currentRow, vector<double>& nextRow) {
	double sum = 0;
	int index = j - 1, col;

	for (int ki = 0; ki < 3; ki++) {
		col = max(0, min(index, m - 1));
;
		sum += previousRow[col] * c[0][ki];
		sum += currentRow[col] * c[1][ki];;
		sum += nextRow[col] * c[2][ki];

		index++;
	}

	return sum;
}

int getStart(int rows, int p, int tid) {
	int rowsProcessedByDefault = rows / p;
	int extraRowsFromPriorThreads = min(tid, rows % p);
	int startPosition = tid * rowsProcessedByDefault + extraRowsFromPriorThreads;

	return startPosition;
}

int getEnd(int rows, int p, int tid) {
	int endPosition = getStart(rows, p, tid) + rows / p;

	bool hasExtraRow = tid < rows % p;
	if (hasExtraRow) {
		endPosition++;
	}

	return endPosition;
}


void sequential(int n, int m, int k) {
	vector<double> previousRow(f[0]);
	vector<double> currentRow(f[0]);
	vector<double> nextRow;

	for (int i = 0; i < n; i++) {
		if (i < n - 1) {
			nextRow = f[i + 1];
		}
;
		for (int j = 0; j < m; j++) {
			f[i][j] = calculateCell(j, m, previousRow, currentRow, nextRow);
		}

		previousRow = currentRow;
		currentRow = nextRow;
	}
}

void run(int tid, int m, int begin, int end,
	vector<double> previousRow, vector<double> currentRow, vector<double> nextRow, vector<double> endRow) {
	
	for (int i = begin; i < end; i++) {
		for (int j = 0; j < m; j++) {
			f[i][j] = calculateCell(j, m, previousRow, currentRow, nextRow);
		}

		previousRow = currentRow;
		currentRow = nextRow;
		
		// + 2 because we are gonna have i+1 on the next run
		if (i + 2 < end) {
			nextRow = f[i + 2];
		}
		else {
			nextRow = endRow;
		}
	}
}

void parallel(int p, int n, int m, int k) {
	if (p <= 0) {
		cout << "Number of threads must be greater than 0." << endl;
		return;
	}

	vector<thread> threads;

	vector<double> previousRow;
	vector<double> currentRow;
	vector<double> nextRow;
	vector<double> endRow;

	for (int tid = 0; tid < p; tid++) {
		int begin = getStart(n, p, tid);
		int end = getEnd(n, p, tid);

		if (begin == 0) {
			previousRow = f[0];
		}
		else {
			previousRow = f[begin - 1];
		}

		currentRow = f[begin];

		nextRow = f[min(begin + 1, n - 1)];

		if (end < n) {
			// copy the first following row that isn't being processed
			// by the current thread since we're modifying f as we're going
			endRow = f[end];
		}
		else {
			// if the end is out of bounds
			// copy the last row of n
			endRow = f[n - 1];
		}

		threads.push_back(thread(run, tid, m, begin, end, previousRow, currentRow, nextRow, endRow));
	}

	for (int i = 0; i < p; i++) {
		threads[i].join();
	}
}

// args = n, m, k, p
int main(int argc, char* argv[])
{
	int n, m, k, p;
	string mode;
	//mode = argv[1];
	//n = atoi(argv[2]);
	//m = atoi(argv[3]);
	//k = atoi(argv[4]);
	//p = atoi(argv[5]);

	mode = "sequential";
	n = 10;
	m = 10;
	k = 3;
	p = 4;

	readMatrices();

	sequential(n, m, k);

	writeMatrix(f, n, m, sequentialOutputFilePath);

	readMatrices();

	auto start = high_resolution_clock::now();
	if (mode == "sequential") {
		sequential(n, m, k);
	}
	else {
		//cout << "running in parallel" << endl;
		parallel(p, n, m, k);
	}

	auto end = high_resolution_clock::now();

	double timeMs = duration_cast<nanoseconds>(end - start).count() / 1000000.0;

	if (!validate(n, m)) {
		cout << "Validation failed!" << endl;
		return 1;
	}

	writeMatrix(f, n, m, outputFilePath);

	cout << timeMs;

}
