#include <iostream>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int a;
	cout << "������� ����� " << endl;
	cin >> a;
	if (a < 0) {
		a = a * (-1);
	}
	if ((a > 99) && (a < 1000))
		cout << "��� �����������";
	else cout<<"��� �� ����������";
}