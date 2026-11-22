#include <chrono>
#include <iostream>
using namespace std;
using namespace std::chrono;

// declare variables
int n=1000;
vector<int> a(n);
vector<int> b(n);
vector<int> c(n);

// allocate vectors by filling them up with random numbers
void allocateVectors() {
  for(int i=0;i<n;i++) {
    a[i] = rand();
    b[i] = rand();
  }
}

// calculate c with the existing vectors
void calculateC() {
  for(int i=0;i<n;i++) {
    c[i] = a[i]+b[i];
  }
}

int main() {
  // internal performance measurement
  // as seen in the example scripts
  auto start =
      high_resolution_clock::now();

  allocateVectors();
  calculateC();

  auto stop =
    high_resolution_clock::now();

  auto duration =
    duration_cast<microseconds>(stop - start)/1000.0;

  cout<<duration.count();
  return 0;
}