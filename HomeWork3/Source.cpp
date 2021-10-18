#include <iostream>
using namespace std;
int Bul(int x,int  a=1) {
	
	if (x > 0) {
		return (x % 10) * a + Bul(x / 10, a * 2);
	}
	else return 0;
}
int main() {
	int x;
	cin >> x;
	cout << Bul(x);
	return 0;
}