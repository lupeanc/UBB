#include <mpi.h>
#include <iostream>

#define TAG_BASIC 0

void recvRecvDeadlock(int rank, int size) {
	int number = 1;

	if (rank == 0) {
		MPI_Recv(&number, 1, MPI_INT, 1, TAG_BASIC, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		
		printf("Process %d received number %d from process 1\n", rank, number);
		number++;

		MPI_Send(&number, 1, MPI_INT, 1, TAG_BASIC, MPI_COMM_WORLD);
	}
	else {
		MPI_Recv(&number, 1, MPI_INT, 0, TAG_BASIC, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

		printf("Process %d received number %d from process 0\n", rank, number);
		number--;

		MPI_Send(&number, 1, MPI_INT, 0, TAG_BASIC, MPI_COMM_WORLD);
	}
}

void sendSendNODeadlock(int rank, int size) {
	int number = 1;

	if (rank == 0) {
		number++;
		MPI_Send(&number, 1, MPI_INT, 1, TAG_BASIC, MPI_COMM_WORLD);
		
		printf("Process %d sent number %d to process 1\n", rank, number);

		MPI_Recv(&number, 1, MPI_INT, 1, TAG_BASIC, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}
	else {
		number--;
		MPI_Send(&number, 1, MPI_INT, 0, TAG_BASIC, MPI_COMM_WORLD);

		printf("Process %d sent number %d to process 0\n", rank, number);

		MPI_Recv(&number, 1, MPI_INT, 0, TAG_BASIC, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}
}

void sendSendDeadlock(int rank, int size) {
	const int N = 10000000;
	int* numbers = new int[N];

	if (rank == 0) {
		MPI_Send(numbers, N, MPI_INT, 1, TAG_BASIC, MPI_COMM_WORLD);

		MPI_Recv(numbers, N, MPI_INT, 1, TAG_BASIC,
			MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}
	else {
		MPI_Send(numbers, N, MPI_INT, 0, TAG_BASIC, MPI_COMM_WORLD);

		MPI_Recv(numbers, N, MPI_INT, 0, TAG_BASIC,
			MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}

	delete[] numbers;
}

int main(int argc, char** argv)
{
	int rank, size;
    MPI_Init(&argc, &argv);

	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	
	sendSendDeadlock(rank, size);
	//recvRecvDeadlock(rank, size);

    MPI_Finalize();
}
