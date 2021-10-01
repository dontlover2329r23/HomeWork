#include <iostream>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int a, b, c, d, r;
	bool bol;
	bol = true;
	cout << "Введите число " << endl;
	cin >> a;
	if (a < 0) {
		a = a * (-1);
	}
	if (a = 0) {
		cout << "Ноль";
	}

	if ((a > 10000000)) {
		bol = false;
		cout << "Ошибка";
	}
	b = a / 1000000;
	if ((b != 0) && (bol == true)) {
		switch (b) {
		case 1: cout << "Один  " << "Миллион";
			break;
		case 2: cout << "Два  " << "Миллиона";
			break;
		case 3: cout << "Три  " << "Миллиона";
			break;
		case 4: cout << "Четыре  " << "Миллиона";
			break;
		case 5: cout << "Пять  ";
			break;
		case 6: cout << "Шесть  ";
			break;
		case 7: cout << "Семь  ";
			break;
		case 8: cout << "Восемь  ";
			break;
		case 9: cout << "Девять  ";
			break;
		case 10: cout << "Десять  ";
			break;


		}
		if (b > 4) {
			cout << "Миллионов";
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
		case 1: cout << "  Сто  ";
			break;
		case 2: cout << "  Двести  ";
			break;
		case 3: cout << "  Триста  ";
			break;
		case 4: cout << "  Четыреста  ";
			break;
		case 5: cout << "  Пятьсот  ";
			break;
		case 6: cout << "  Шестьсот  ";
			break;
		case 7: cout << "  Семьсот  ";
			break;
		case 8: cout << "  Восемьсот  ";
			break;
		case 9: cout << "  Девятьсот  ";
			break;



		}
		switch (d) {

		case 2: cout << "  Двадцать  ";
			break;
		case 3: cout << "  Тридцать  ";
			break;
		case 4: cout << "  Сорок  ";
			break;
		case 5: cout << "  Пятьдесят  ";
			break;
		case 6: cout << "  Шестьдесят  ";
			break;
		case 7: cout << "  Семьдесят  ";
			break;
		case 8: cout << "  Восемьдесят  ";
			break;
		case 9: cout << "  Девяносто  ";
			break;
		}
		if ((d == 1) && (r == 0)) {
			cout << "  Десять  ";
		}
		if ((d == 1) && (r > 0)) {
			switch (r) {
			case 1: cout << "  Одинадцать  " << "Тысяч";
				break;
			case 2: cout << "  Двенадцать  " << "Тысяч";
				break;
			case 3: cout << "  Тринадцать  " << "Тысяч";
				break;
			case 4: cout << "  Четырнадцать  " << "Тысяч";
				break;
			case 5: cout << "  Пятнадцать  " << "Тысяч";
				break;
			case 6: cout << "  Шестнадцать  " << "Тысяч";
				break;
			case 7: cout << "  Семнадцать  " << "Тысяч";
				break;
			case 8: cout << "  Восемнадцать  " << "Тысяч";
				break;
			case 9: cout << "  Девятнадцать  " << "Тысяч";
				break;
			}
		}
		if (d != 1) {
			switch (r) {
			case 1: cout << "  Одна  " << "Тысяча  ";
				break;
			case 2: cout << "  Две  " << "Тысячи  ";
				break;
			case 3: cout << "  Три  " << "Тысячи  ";
				break;
			case 4: cout << "  Четыре  " << "Тысячи  ";
				break;
			case 5: cout << "  Пять  " << "Тысяч  ";
				break;
			case 6: cout << "  Шесть  " << "Тысяч  ";
				break;
			case 7: cout << "  Семь  " << "Тысяч  ";
				break;
			case 8: cout << "  Восемь   " << "Тысяч   ";
				break;
			case 9: cout << "  Девять   " << "Тысяч  ";
				break;
			}

		}
		if ((r == 0) && ((b > 0) || (d > 0))) {
			cout << "Тысяч";
		}
	}
	b = a / 100;
	a = a - 100 * b;
	d = a / 10;
	a = a - 10 * d;
	r = a;
	if ((bol == true)) {
		switch (b) {
		case 1: cout << "  Сто  ";
			break;
		case 2: cout << "  Двести  ";
			break;
		case 3: cout << "  Триста  ";
			break;
		case 4: cout << "  Четыреста  ";
			break;
		case 5: cout << "  Пятьсот  ";
			break;
		case 6: cout << "  Шестьсот  ";
			break;
		case 7: cout << "  Семьсот  ";
			break;
		case 8: cout << "  Восемьсот  ";
			break;
		case 9: cout << "  Девятьсот  ";
			break;



		}
		switch (d) {

		case 2: cout << "  Двадцать  ";
			break;
		case 3: cout << "  Тридцать  ";
			break;
		case 4: cout << "  Сорок  ";
			break;
		case 5: cout << "  Пятьдесят  ";
			break;
		case 6: cout << "  Шестьдесят  ";
			break;
		case 7: cout << "  Семьдесят  ";
			break;
		case 8: cout << "  Восемьдесят  ";
			break;
		case 9: cout << "  Девяносто  ";
			break;
		}
		if ((d == 1) && (r == 0)) {
			cout << "  Десять  ";
		}
		if ((d == 1) && (r > 0)) {
			switch (r) {
			case 1: cout << "  Одинадцать  ";
				break;
			case 2: cout << "  Двенадцать  ";
				break;
			case 3: cout << "  Тринадцать  ";
				break;
			case 4: cout << "  Четырнадцать  ";
				break;
			case 5: cout << "   Пятнадцать  ";
				break;
			case 6: cout << "  Шестнадцать  ";
				break;
			case 7: cout << "   Семнадцать  ";
				break;
			case 8: cout << "   Восемнадцать  ";
				break;
			case 9: cout << "  Девятнадцать  ";
				break;
			}
		}
		if (d != 1) {
			switch (r) {
			case 1: cout << "  один  ";
				break;
			case 2: cout << "  Два  ";
				break;
			case 3: cout << "  Три  ";
				break;
			case 4: cout << "  Четыре  ";
				break;
			case 5: cout << "  Пять  ";
				break;
			case 6: cout << "   Шесть   ";
				break;
			case 7: cout << "   Семь  ";
				break;
			case 8: cout << "   Восемь";
				break;
			case 9: cout << "   Девять   ";
				break;
			}

		}

	}

	return 0;

}
