#include <iostream>
#include <chrono>
#include <stdlib.h>
#include <thread>
#include <mutex>
using namespace std;
using namespace std::chrono;

#define N 100000000
#define P 4
mutex mtx;
double RESULT = 0.0;
//const int N = 100000;

//double a[N], b[N];
//vector<double> a(N), b(N);

void init(double *v)
{
    for (int i = 0; i < N; i++)
    {
        v[i] = rand()%1000;
    }
}

double dot_product(double* v1, double* v2)
{
	double sum = 0.0;
    for (int i = 0; i < N; i++) {
		sum += v1[i] * v2[i];
    }

	return sum;
}

void worker(double* a, double* b, int start_index, int end_index) {
	double sum = 0.0;
	for (int i = start_index; i < end_index; i++) {
		sum += a[i] * b[i];
	}

	//mtx.lock();
	// 
	// Use lock_guard to automatically manage the mutex lock
	// basically keeps the lock until the }
	lock_guard<mutex> guard(mtx);
	RESULT += sum;
	//mtx.unlock();
}

int main()
{
	double* a = new double[N];
	double* b = new double[N];

    init(a);
	init(b);

	auto start = high_resolution_clock::now();
	//double result = dot_product(a, b);
	//auto end = high_resolution_clock::now();

	int chunk_size = N / P;
	int remainder = N % P;

	int start_index = 0;
	int end_index = chunk_size;

	thread threads[P];
	for (int i = 0; i < P; i++) {
		if (remainder > 0) {
			end_index++;
			remainder--;
		}

		threads[i] = thread(worker, a, b, start_index, end_index);
	}

	for (int i = 0; i < P; i++) {
		threads[i].join();
	}

	auto end = high_resolution_clock::now();

	double duration = duration_cast<nanoseconds>(end - start).count()/1000000.0;

	//cout << "Dot product: " << result << endl;
	cout << "Dot product: " << RESULT << endl;
	cout << "Duration: " << duration << " ms" << endl;

	delete[] a;
	delete[] b;

    return 0;
}