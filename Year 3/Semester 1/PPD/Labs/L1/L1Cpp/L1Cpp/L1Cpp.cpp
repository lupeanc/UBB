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
#define CONV_MAX 5

//int f[MAX][MAX];
//int c[CONV_MAX][CONV_MAX];
vector<vector<int>> f(MAX, vector<int>(MAX));
vector<vector<int>> c(CONV_MAX, vector<int>(CONV_MAX));
vector<vector<int>> v(MAX, vector<int>(MAX));

#define matrixFFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\MatrixF.txt"
#define convMatrixFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\ConvolutionM.txt"
#define outputFilePath "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\output.txt"

void readMatrices() {
	ifstream matrixFFile(matrixFFilePath);
	ifstream convMatrixFile(convMatrixFilePath);
	
	vector<vector<int>> matrixF;
	vector<vector<int>> convMatrix;
	string line;

	// read matrix F
	if (matrixFFile.is_open()) {
		while (getline(matrixFFile, line)) {
			if (line.empty()) {
				continue; // Skip empty lines
			}

			stringstream lineStream(line);
			vector<int> values;
			string value;

			while(lineStream >> value) {
				values.push_back(atoi(value.c_str()));
			}

			//if (!values.empty()) {
			//	f.push_back(values);
			//}

			if (!values.empty()) {
				matrixF.push_back(values);
			}
		}

		for (int i = 0; i < matrixF.size() && i < MAX; i++) {
			for (int j = 0; j < matrixF[i].size() && j < MAX; j++) {
				f[i][j] = matrixF[i][j];
			}
		}
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
			vector<int> values;
			string value;

			while (lineStream >> value) {
				values.push_back(atoi(value.c_str()));
			}

			//if (!values.empty()) {
			//	c.push_back(values);
			//}

			if (!values.empty()) {
				convMatrix.push_back(values);
			}

		}

		for (int i = 0; i < convMatrix.size() && i < CONV_MAX; i++) {
			for (int j = 0; j < convMatrix[i].size() && j < CONV_MAX; j++) {
				c[i][j] = convMatrix[i][j];
			}
		}
	}
	else {
		cout << "Unable to open file: " << convMatrixFilePath << endl;
	}
}

vector<vector<int>> copyMatrix(const vector<vector<int>>& matrix) {
	int rows = matrix.size();
	int cols = matrix[0].size();
	vector<vector<int>> newMatrix(rows, vector<int>(cols));
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			newMatrix[i][j] = matrix[i][j];
		}
	}
	return newMatrix;
}

void writeMatrix(vector<vector<int>> matrix, int n, int m) {
	ofstream outputFile(outputFilePath);
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

int getValueOfCurrentCell(int i, int j, int n, int m) {
	i = max(0, min(i, n - 1));
	j = max(0, min(j, m - 1));
	return f[i][j];
}

void calculateCell(int i, int j, int k, int n, int m) {
	int sum = 0, radius = k / 2;

	for (int ki = 0; ki < k; ki++) {
		for (int kj = 0; kj < k; kj++) {
			int fi = i + ki - radius;
			int fj = j + kj - radius;
			sum += getValueOfCurrentCell(fi, fj, n, m) * c[ki][kj];
		}
	}

	v[i][j] = sum;
}

bool validate(const vector<vector<int>> expected, const vector<vector<int>> actual) {
	for (int i = 0; i < expected.size(); i++) {
		for (int j = 0; j < expected[i].size(); j++) {
			if (expected[i][j] != actual[i][j]) {
				cout << "Validation failed at cell (" << i << ", " << j << "): expected " << expected[i][j] << ", got " << actual[i][j] << endl;
				return false;
			}
		}
	}
	return true;
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
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			calculateCell(i, j, k, n, m);
		}
	}
}

void run(int tid, int p, string mode, int n, int m, int k) {
	if (mode == "horizontal") {
		int startRow = getStart(n, p, tid);
		int endRow = getEnd(n, p, tid);

		for (int i = startRow; i < endRow; i++) {
			for (int j = 0; j < m; j++) {
				calculateCell(i, j, k, n, m);
			}
		}
	}
	else if (mode == "vertical") {
		int startCol = getStart(m, p, tid);
		int endCol = getEnd(m, p, tid);

		for (int i = 0; i < n; i++) {
			for (int j = startCol; j < endCol; j++) {
				calculateCell(i, j, k, n, m);
			}
		}
	}
	else {
		cout << "Invalid mode: " << mode << endl;
	}
}

void parallel(int p, string mode, int n, int m, int k) {
	if (p <= 0) {
		cout << "Number of threads must be greater than 0." << endl;
		return;
	}

	vector<thread> threads;

	for (int tid = 0; tid < p; tid++) {
		threads.push_back(thread(run, tid, p, mode, n, m, k));
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
	mode = argv[1];
	n = atoi(argv[2]);
	m = atoi(argv[3]);
	k = atoi(argv[4]);
	p = atoi(argv[5]);
	//mode = "sequential";
	//n = 10000;
	//m = 10000;
	//k = 5;
	//p = 4;

	//cout << "reading" << endl;
	readMatrices();

	sequential(n, m, k);
	vector<vector<int>> expected = copyMatrix(v);
	
	auto start = high_resolution_clock::now();
	if (mode == "sequential") {
		//cout << "running sequentially" << endl;
		sequential(n, m, k);
	}
	else {
		//cout << "running in parallel" << endl;
		parallel(p, mode, n, m, k);
	}

	auto end = high_resolution_clock::now();

	double timeMs = duration_cast<nanoseconds>(end - start).count() / 1000000.0;

	//cout << "validating" << endl;
	if (!validate(expected, v)) {
		cout << "Validation failed!" << endl;
		return 1;
	}

	//cout << "got here"<<endl;
	writeMatrix(v, n, m);

	cout << timeMs;
}
