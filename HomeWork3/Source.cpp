#include <iostream>
using namespace std;
int Del(int x,int  a) {
	if (x > 1) {
		if (x % a == 0) {
			cout << a << " * ";
			Del(x / a, a);
			return a, x;
		}
		else {
			Del(x, a + 1);
			return a, x;
		}
	}
	if (x == 1) return a, x;
}
int main() {
	int x, a;
	a = 2;
	cin >> x;
	if (x == 1)
		cout << "1";
	if (x > 1) {
		cout << "x= ";
		Del(x, a);
	}
	return 0;
}