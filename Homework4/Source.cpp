#include <iostream>
#include <ctime>
using namespace std;
void print_arr(int A[], int N) {
	for (int i = 0; i < N; i++) {
		cout << "A[" << i << "]" << " = " << A[i] << endl;
	}
}
void Arif(int a1, int d, int A[], int N) {
	A[0] = a1;
	for (int i = 1; i < N; i++) {
		A[i] = d + A[i - 1];

	}

}
int random(int B) {
	return rand() % B;
}
void zad1(int a1, int d, int A [] , int N) {
	Arif(a1, d, A, N);
	print_arr(A, N);
}
void zad2(int A[], int N) {
	bool already;
	for (int i = 0; i < N;) {
		already = false;
		int m = random(N) + 1;
		for (int k = 0; k < i; k++) {
			if (A[k] == m)
				already = true;
		}
		if (!already) {
			A[i] = m;
			i++;
		}
	}
	print_arr(A, N);
}
void zad3( int A[], int N) {
	for (int i = 0; i < N; i++) {
		A[i] = random(2000) + 1000;

	}
	int k = 0;
	for (int i = 0; i < N; i++) {
		int b = A[i] / 10;
		int c = b % 10;
		if (c % 2 == 0) {
			k += 1;
		}

	}
	print_arr(A, N);
	cout << endl;
	cout << "the number of elements whose second digit from the end is even-" << k;
}
int main() {
	
	srand(static_cast<unsigned int>(time(0)));
	const int N = 60;
	cout << "enter the number of elements ";
	
	int A[N];
	int d, a1;
	
		cout << "enter the difference ";
		cin >> d;
		cout << "enter the first element ";
		cin >> a1;
		cout << "task 1" << endl;
		zad1(a1, d, A, N);
		cout << "task 2" << endl;
		zad2( A, N);
		cout << "task 3"<<endl;
		zad3(A, N);
	return 0;
}
