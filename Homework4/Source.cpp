#include <iostream>
#include <ctime>
using namespace std;
void print_arr(int A[],  int N) {
	for (int i = 0; i < N; i++) {
		cout << "A[" << i << "]" << " = " << A[i] << endl;
	}
}
void Arif(int a1 , int d,int A[],  int N) {
	A[0] = a1;
	for (int i = 1; i < N; i++) {
		A[i] = d + A[i - 1];
	}
			
}
int random(int B) {
	return rand() % B;
}
int main() {
	const int N = 60;
	srand(static_cast<unsigned int>(time(0)));
	int A[N];
	bool already;
	int d, a1 , x;
	cout << "enter 1 - to complete the first task; "<<endl;
	cout << "2 - to complete the second task;" << endl;
	cout << "3 - to complete the third task;" << endl;
	cin >> x;
	if (x == 1) {
		cout << "enter the difference";
		cin >> d;
		cout << "enter the first element";
		cin >> a1;
		Arif(a1, d, A, N);
		print_arr(A, N);
	}
	if (x == 2) {
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
	if (x == 3) {
		for(int i = 0; i < N; i++) {
			A[i] = random(2000) + 1000;
			
		}
		int k = 0;
		for (int i = 0; i < N; i++) {
			int b = A[i] / 10;
			int c = b % 10;
			if (c%2==0 ) {
				k += 1;
			}

		}
		cout << "the number of elements whose second digit from the end is even-" << k;

	}
	
	return 0;
}