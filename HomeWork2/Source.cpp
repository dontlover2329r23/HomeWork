#include <iostream>
using namespace std;
int del1(int a) {
	int i;
	int sum = 0;
	for (i = 1; i < a; i++) {
		if (a % i == 0)
			sum += i;
	}
	return sum;
}
int del2(int b) {
	int i;
	int sum = 0;
	for (i = 1; i < b; i++) {
		if (b % i == 0)
			sum += i;
	}
	return sum;
}
int main() {
	setlocale(LC_ALL, "ru");
	int x, y, a, b, i, j;
	j = 0;
	for (i = 1; i <= 10000; i++) {
		    a = i;
			x = del1(a);
			b = x;
			y = del2(b);
			if (a!=j) {
				if ((a == y) && (a != x)) {
					j = b;
					cout << a << " " << b << endl;
				}
			}
			x = 0;
			y = 0;
		
	}
}
