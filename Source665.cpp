#include<iostream>
using namespace std;
int FIBONACHI(int e)
{
	int a;
	int b = 0;
	int c = 1;
	int d = 1;
	if (e > 0) {
		while (b != e - 1) {
			a = c;
			c = c + d;
			d = a;
			b++;
		}
		return d;
	}
	else
		return 0;
}


int main() {
	setlocale(LC_ALL, "ru");
	int a , b;
	cout<<"enter a number";
	cin >> a;
	cout<<"fibonacci numbers-"<<FIBONACHI(a);
	
	return 0;
}
