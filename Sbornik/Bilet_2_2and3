// Bilet #2
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

template <typename T>
void print_array(T* array, const int N) {

    for (int index = 0; index < N; index++ ) {

        cout << array[index] << " ";

    }
    cout << endl;
}

int find_scale() {

    ifstream fin("task1.txt");

    if (!fin.is_open()) {
        cout << "Error";
        exit(-1);
    }

    string tmp;
    int scale = 0;

    while (!fin.eof()) {

        fin >> tmp;

        if (!fin.fail()) {

            scale++;

        }

    }

    return scale;
}

void fill_array_from_txt(int* &array, const int &scale) {


    ifstream fin("task1.txt");

    if (!fin.is_open()) {
        cout << "Error";
        exit(-1);
    }

    string tmp;
    int index = 0;

    while (!fin.eof()) {

        fin >> tmp;

        if (!fin.fail()) {

            array[index] = stoi(tmp);
            index++;
        }

    }

}

bool one_line(int& x1,int& x2,int& x3,int& y1,int& y2,int& y3) {

    // x3 - x1      y3 - y1
    // ______   =   _______
    // x2 - x1      y2 - y1

    if (x2 == x1 || y2 == y1) {
        swap(x2,x3);
        one_line(x1, x2, x3, y1, y2, y3);
    }
    else if (x2 != x1 && y2 != y1) {

        if ((x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1)) {
            return false;
        }

        else {
        return true;
        }

    }
}

double distance_t(const int &x1,const int &x2,const int &y1,const int &y2) {
   return sqrt( pow((x2-x1),2) + pow((y2-y1),2) );
}

void perimeter(int* &array, const int &scale) {

    int x1,x2,x3 = 0;
    int y1,y2,y3 = 0;

    int x1_max,x2_max,x3_max;
    int y1_max,y2_max,y3_max;

    double perimeter_triangle = INT_MIN;

    for (int index_1 = 0; index_1 < scale - 1 - 4; index_1 += 2) {

        x1 = array[index_1]; y1 = array[index_1+1];

        for (int index_2 = index_1 + 2; index_2 < scale - 1 - 2; index_2 += 2) {
            x2 = array[index_2]; y2 = array[index_2+1];

            for (int index_3 = index_2 + 2; index_3 < scale - 1; index_3 += 2) {
                x3 = array[index_3]; y3 = array[index_3+1];

                if (one_line(x1,x2,x3,y1,y2,y3) == true) {
                    //cout << "(" << x1 << ";" << y1 << ")" << "(" << x2 << ";" << y2 << ")" << "(" << x3 << ";" << y3 << ")" << endl;

                    double perimeter_triangle_tmp = distance_t(x1,x2,y1,y2) + distance_t(x2,x3,y2,y3) + distance_t(x1,x3,y1,y3);

                    if (perimeter_triangle_tmp > perimeter_triangle) {
                        perimeter_triangle = perimeter_triangle_tmp;
                        x1_max = x1; x2_max = x2; x3_max = x3;
                        y1_max = y1; y2_max = y2; y3_max = y3;
                        //cout << perimeter_triangle_tmp << " = tmp" << endl;
                        //cout << perimeter_triangle << " = max" << endl << endl;
                    }
                    else{
                        //cout << perimeter_triangle_tmp << " = tmp" << endl;
                        //cout << perimeter_triangle << " = max" << endl << endl;
                    }
                }
                else {
                    continue;
                }
            }
        }
    }

    cout << endl << "Max perimeter = " << perimeter_triangle << endl;
    cout << "x1 = " << x1_max << "; x2 = " << x2_max << "; x3 = " << x3_max << endl;
    cout << "y1 = " << y1_max << "; y2 = " << y2_max << "; y3 = " << y3_max << endl;
}

void task1() {

    int scale = find_scale();

    int* array = new int[scale];

    fill_array_from_txt(array,scale);

    print_array(array,scale);
    cout << endl;
    perimeter(array,scale);

}

// ///////////////////////////////////////////////////

void work_with_string(string &str, const string &word) {

    string tmp;

    for (int index = 0; index < str.size(); index++) {

        if (str[index] != '!' && str[index] != '?' && str[index] != '.') {
            tmp += str[index];
        }

        else {
            if (tmp.size() > 0) {
            for (int index_2 = 0; index_2 < tmp.size(); index_2++) {
                    if (tmp[index_2] == word[0]) {
                        int flag = 0;

                        for (int index_3 = 0; index_3 < word.size(); index_3++) {
                            if (tmp[index_2 + index_3] != word[index_3]) {
                                flag = 1;
                            }
                        }

                        if (flag == 0) {
                            cout << tmp + str[index];
                            break;
                        }

                        else {
                            continue;
                        }
                    }
            }
            }
            tmp = "";
        }

    }

}

void task2() {

    ifstream fin("task2.txt");

    if (!fin.is_open()) {
        cout << "error";
        exit(-1);
    }

    string tmp;

    while (!fin.eof()) {

        getline(fin,tmp);
        work_with_string(tmp,"Bob");
    }

}

int main() {

    //ofstream("task1.txt");
    //ofstream("task2.txt");

    task1();
    cout << endl;
    task2();
}
