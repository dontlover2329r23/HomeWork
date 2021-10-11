#include <iostream>
using namespace std;
int del1(int a){
	int i;
	int sum = 0;
	for (i = 0; i < a; i++) {
		if (a % i == 0)
			sum += i;
	}
	return sum;
}
int del2(int b) {
	int i;
	int sum = 0;
	for (i = 0; i < b; i++) {
		if (b % i == 0)
			sum += i;
	}
	return sum;
}
int main() {
	setlocale(LC_ALL, "ru");
	int x, y, a, b;
	cout << "Enter two numbers";
	cin >> a >> b;
	x = del1(a);
	y = del2(b);
	if ((a = y) && (b = x)) {
		cout << "These are friendly numbers!";
	}
	else
		cout << "These are not friendly numbers!";
}