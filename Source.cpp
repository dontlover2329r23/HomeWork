#include <iostream>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int a, b, c, d, r;
	bool bol;
	bol = true;
	cout << "������� ����� " << endl;
	cin >> a;
	if (a < 0) {
		a = a * (-1);
	}
	if (a = 0) {
		cout << "����";
	}

	if ((a > 10000000)) {
		bol = false;
		cout << "������";
	}
	b = a / 1000000;
	if ((b != 0) && (bol == true)) {
		switch (b) {
		case 1: cout << "����  " << "�������";
			break;
		case 2: cout << "���  " << "��������";
			break;
		case 3: cout << "���  " << "��������";
			break;
		case 4: cout << "������  " << "��������";
			break;
		case 5: cout << "����  ";
			break;
		case 6: cout << "�����  ";
			break;
		case 7: cout << "����  ";
			break;
		case 8: cout << "������  ";
			break;
		case 9: cout << "������  ";
			break;
		case 10: cout << "������  ";
			break;


		}
		if (b > 4) {
			cout << "���������";
		}
	}
	a = a - 1000000 * b;
	b = a / 100000;
	a = a - 100000 * b;
	d = a / 10000;
	a = a - 10000 * d;
	r = a / 1000;
	a = a - 1000 * r;

	if ((bol == true)) {
		switch (b) {
		case 1: cout << "  ���  ";
			break;
		case 2: cout << "  ������  ";
			break;
		case 3: cout << "  ������  ";
			break;
		case 4: cout << "  ���������  ";
			break;
		case 5: cout << "  �������  ";
			break;
		case 6: cout << "  ��������  ";
			break;
		case 7: cout << "  �������  ";
			break;
		case 8: cout << "  ���������  ";
			break;
		case 9: cout << "  ���������  ";
			break;



		}
		switch (d) {

		case 2: cout << "  ��������  ";
			break;
		case 3: cout << "  ��������  ";
			break;
		case 4: cout << "  �����  ";
			break;
		case 5: cout << "  ���������  ";
			break;
		case 6: cout << "  ����������  ";
			break;
		case 7: cout << "  ���������  ";
			break;
		case 8: cout << "  �����������  ";
			break;
		case 9: cout << "  ���������  ";
			break;
		}
		if ((d == 1) && (r == 0)) {
			cout << "  ������  ";
		}
		if ((d == 1) && (r > 0)) {
			switch (r) {
			case 1: cout << "  ����������  " << "�����";
				break;
			case 2: cout << "  ����������  " << "�����";
				break;
			case 3: cout << "  ����������  " << "�����";
				break;
			case 4: cout << "  ������������  " << "�����";
				break;
			case 5: cout << "  ����������  " << "�����";
				break;
			case 6: cout << "  �����������  " << "�����";
				break;
			case 7: cout << "  ����������  " << "�����";
				break;
			case 8: cout << "  ������������  " << "�����";
				break;
			case 9: cout << "  ������������  " << "�����";
				break;
			}
		}
		if (d != 1) {
			switch (r) {
			case 1: cout << "  ����  " << "������  ";
				break;
			case 2: cout << "  ���  " << "������  ";
				break;
			case 3: cout << "  ���  " << "������  ";
				break;
			case 4: cout << "  ������  " << "������  ";
				break;
			case 5: cout << "  ����  " << "�����  ";
				break;
			case 6: cout << "  �����  " << "�����  ";
				break;
			case 7: cout << "  ����  " << "�����  ";
				break;
			case 8: cout << "  ������   " << "�����   ";
				break;
			case 9: cout << "  ������   " << "�����  ";
				break;
			}

		}
		if ((r == 0) && ((b > 0) || (d > 0))) {
			cout << "�����";
		}
	}
	b = a / 100;
	a = a - 100 * b;
	d = a / 10;
	a = a - 10 * d;
	r = a;
	if ((bol == true)) {
		switch (b) {
		case 1: cout << "  ���  ";
			break;
		case 2: cout << "  ������  ";
			break;
		case 3: cout << "  ������  ";
			break;
		case 4: cout << "  ���������  ";
			break;
		case 5: cout << "  �������  ";
			break;
		case 6: cout << "  ��������  ";
			break;
		case 7: cout << "  �������  ";
			break;
		case 8: cout << "  ���������  ";
			break;
		case 9: cout << "  ���������  ";
			break;



		}
		switch (d) {

		case 2: cout << "  ��������  ";
			break;
		case 3: cout << "  ��������  ";
			break;
		case 4: cout << "  �����  ";
			break;
		case 5: cout << "  ���������  ";
			break;
		case 6: cout << "  ����������  ";
			break;
		case 7: cout << "  ���������  ";
			break;
		case 8: cout << "  �����������  ";
			break;
		case 9: cout << "  ���������  ";
			break;
		}
		if ((d == 1) && (r == 0)) {
			cout << "  ������  ";
		}
		if ((d == 1) && (r > 0)) {
			switch (r) {
			case 1: cout << "  ����������  ";
				break;
			case 2: cout << "  ����������  ";
				break;
			case 3: cout << "  ����������  ";
				break;
			case 4: cout << "  ������������  ";
				break;
			case 5: cout << "   ����������  ";
				break;
			case 6: cout << "  �����������  ";
				break;
			case 7: cout << "   ����������  ";
				break;
			case 8: cout << "   ������������  ";
				break;
			case 9: cout << "  ������������  ";
				break;
			}
		}
		if (d != 1) {
			switch (r) {
			case 1: cout << "  ����  ";
				break;
			case 2: cout << "  ���  ";
				break;
			case 3: cout << "  ���  ";
				break;
			case 4: cout << "  ������  ";
				break;
			case 5: cout << "  ����  ";
				break;
			case 6: cout << "   �����   ";
				break;
			case 7: cout << "   ����  ";
				break;
			case 8: cout << "   ������";
				break;
			case 9: cout << "   ������   ";
				break;
			}

		}

	}

	return 0;

}
