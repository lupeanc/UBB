#include <iostream>
#include <fstream>

using namespace std;

#define NUMBER_1_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar1.txt"
#define NUMBER_2_FILE "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L3\\Numar2.txt"

int main()
{
	ofstream number1File(NUMBER_1_FILE);
	ofstream number2File(NUMBER_2_FILE);

	int N1 = 100;
	int N2 = 100000;
	int digit;

	number1File << N1 << " ";

	for (int i = 0; i < N1; i++)
	{
		digit = rand() % 10;
		number1File << digit << " ";
	}

	number2File << N2 << " ";

	for (int i = 0; i < N2; i++)
	{
		digit = rand() % 10;
		number2File << digit << " ";
	}

	number1File.close();
	number2File.close();
}
