#include<iostream>
#include<ctime>
#include <stdlib.h> 
using namespace std;
int GetRandomNumber(int min, int max)
{
	srand(time(NULL));
	int num = min + rand() % (max - min + 1);
	return num;
}


void main() {
	setlocale(LC_ALL, "ru");
	int b;
	b = GetRandomNumber(1, 6);
	int a;
	a = GetRandomNumber(1,6);
	cout <<"The first roll of the dice-"<< a<< endl;
	cout << "The second roll of the dice-"<<b;
	

	
}
