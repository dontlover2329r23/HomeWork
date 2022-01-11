#include <iostream>
#include <fstream>
#include <ctime>

// https://www.cyberforum.ru/cpp-beginners/thread2354704.html - по поводу бинарного файла и матрицы.

using namespace std;
void del_array(int** &array, int str, int col) {
    for (int i = 0; i < str; i++)
        delete[] array[i];

    delete[] array;
}

int random() {
    return rand()%15 + 1;
}
void print_matrix(int **matrix, const int size_str, const int size_col) {
    for (int str = 0; str < size_str; str++) {
        for (int col = 0; col < size_col; col++) {
            cout << matrix[str][col] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}
void initialization_random(int **matrix, const int size_str, const int size_col) {
    for (int str = 0; str < size_str; str++) {
        for (int col = 0; col < size_col; col++) {
            matrix[str][col] = random();
        }
    }
}
// ///////////////////////

void write_matrix_in_file(int** matrix, const int &size_str, const int &size_col) {

    ofstream fout("task1.txt");

    if (!fout.is_open()) {
        cout << "error";
        exit(-1);
    }

    for (int str = 0; str < size_str; str++) {
        for (int col = 0; col < size_col; col++) {

            fout << matrix[str][col] << " ";

        }
        fout << "\n";
    }
}

void recieve_matrix_from_file(int** &matrix, const int size_str, const int size_col) {

    ifstream fin("task1.txt");

    if (!fin.is_open()) {
        cout << "Error!" << endl;
        exit(-1);
    }

    int str = 0;
    string line;

    while(!fin.eof()) {

        string tmp;
        int col = 0;

        getline(fin,line);

        for (int index = 0; index < line.size(); index++) {

            if (line[index] != ' ') {
                tmp += line[index];
            }

            else {
                matrix[str][col] = stoi(tmp);
                tmp = "";
                col++;
            }

        }

        if (tmp.size() > 0) matrix[str][size_col-1] = stoi(tmp);

        str++;
    }

    print_matrix(matrix,size_str,size_col);
}

void swap_col_min_max(int** &matrix, const int &size_str, const int &size_col) {

    int col_1 = -1;
    int col_2 = -1;

    int minimal = INT_MAX;
    int maximal = INT_MIN;

    for (int str = 0; str < size_str; str++) {
        for (int col = 0; col < size_col; col++) {

            if (matrix[str][col] < minimal) {
                minimal = matrix[str][col];
            }

            if (matrix[str][col] > maximal) {
                maximal = matrix[str][col];
            }
        }
    }

    for (int col = 0; col < size_col; col++) {
        int flag1 = 0;
        int flag2 = 0;
        for (int str = 0; str < size_str; str++) {

            if (matrix[str][col] == minimal) {
                flag1 = 1;
            }

            else if (matrix[str][col] == maximal) {
                flag2 = 1;
            }

        }
        if (flag1 == 1 && flag2 == 1) {
            if (col_1 == -1) {
            col_1 = col;
            }
            else {
            col_2 = col;
            }
        }
    }
    if (col_1 != -1 && col_2 != -1) {

        cout << col_1 << " " << col_2 << endl;

        for (int str = 0; str < size_str; str++) {

            swap(matrix[str][col_1], matrix[str][col_2]);

        }
    }
    else {
        cout << "I cant do it!" << endl;
        exit(-1);
    }

    print_matrix(matrix,size_str,size_col);
}

void task1() {
    srand(time(NULL));
    int size_str, size_col;

    size_str = 5;
    size_col = 4;

    // Initialization
    int** matrix_start = new int* [size_str];
    for (int i = 0; i < size_str; i++) {
        matrix_start[i] = new int[size_col];
    }

    // Fill matrix
    initialization_random(matrix_start,size_str,size_col);

    // Write matrix to file
    write_matrix_in_file(matrix_start, size_str, size_col);

    // Delete matrix
    for (int i = 0; i < size_col; i++) {
        delete []matrix_start[i];
    }
    delete []matrix_start;

    // Initialization
    int** matrix = new int* [size_str];
    for (int i = 0; i < size_str; i++) {
        matrix[i] = new int[size_col];
    }

    // Fill matrix from file
    recieve_matrix_from_file(matrix,size_str,size_col);
    swap_col_min_max(matrix,size_str,size_col);
}

// /////////////////////////////////////////////////

void create_bin_files() {

    ofstream ("task2_1.dat");
    ofstream ("task2_2.dat");
    ofstream ("task2_3.dat");

}

void write_matrix_in_bin_file(int** matrix, const int &size_str, const int &size_col, string file) {

    ofstream fout(file,ios_base::binary);

    if (!fout.is_open()) {
        cout << "error";
        exit(-1);
    }

    int tmp;

    for (int str = 0; str < size_str; str++) {

        for (int col = 0; col < size_col; col++) {
            tmp = matrix[str][col];
            fout.write((char*)&tmp, sizeof(tmp));

        }

    }

}

void fill_matrix_from_bin_file(int** &matrix, const int size_str, const int size_col, string file) {

    int tmp;

    ifstream fin(file,ios_base::binary);

    for(int i = 0; i < size_str; i++) {
        for(int j = 0; j < size_col; j++) {
            fin.read((char*)&matrix[i][j], sizeof(int));
        }
    }
    fin.close();

    print_matrix(matrix,size_str,size_col);

}

void multiply(int **matrix_1, int**matrix_2, int** &matrix_result, const int size_str_1, const int size_col_1, const int size_str_2, const int size_col_2) {

    int m = size_col_1;

    for (int i = 0; i < size_str_1; i++) {
        for (int j = 0; j < size_col_2; j++) {

            int element_of_mltp = 0;
            for (int r = 0; r < m; r++) {
                element_of_mltp += matrix_1[i][r] * matrix_2[r][j];
            }

            matrix_result[i][j] = element_of_mltp;

        }

    }

    print_matrix(matrix_result,size_str_1,size_col_2);
}

void task2() {

    int size_str_1 = 4;
    int size_col_1 = 3;

    int size_str_2 = 3;
    int size_col_2 = 5;

    create_bin_files();

    // Initialization
    int** matrix_1 = new int* [size_str_1];
    for (int i = 0; i < size_str_1; i++) {
        matrix_1[i] = new int[size_col_1];
    }

    int** matrix_2 = new int* [size_str_2];
    for (int i = 0; i < size_str_2; i++) {
        matrix_2[i] = new int[size_col_2];
    }

    initialization_random(matrix_1,size_str_1,size_col_1);
    initialization_random(matrix_2,size_str_2,size_col_2);

    write_matrix_in_bin_file(matrix_1,size_str_1,size_col_1,"task2_1.dat");
    write_matrix_in_bin_file(matrix_2,size_str_2,size_col_2,"task2_2.dat");

    // Delete matrix
    del_array(matrix_1,size_str_1,size_col_1);
    del_array(matrix_2,size_str_2,size_col_2);

    if (size_col_1 == size_str_2) {

        int** matrix_11 = new int* [size_str_1];
        for (int i = 0; i < size_str_1; i++) {
            matrix_11[i] = new int[size_col_1];
        }

        int** matrix_22 = new int* [size_str_2];
        for (int i = 0; i < size_str_2; i++) {
            matrix_22[i] = new int[size_col_2];
        }

        int size_str_result = size_str_1;
        int size_col_result = size_col_2;

        int** matrix_result = new int* [size_str_result];
        for (int i = 0; i < size_str_result; i++) {
            matrix_result[i] = new int[size_col_result];
        }

        fill_matrix_from_bin_file(matrix_11,size_str_1,size_col_1,"task2_1.dat");
        fill_matrix_from_bin_file(matrix_22,size_str_2,size_col_2,"task2_2.dat");

        multiply(matrix_11,matrix_22,matrix_result,size_str_1,size_col_1,size_str_2,size_col_2);

        write_matrix_in_bin_file(matrix_result,size_str_1,size_col_2,"task2_3.dat");
    }

    else {
        exit(-1);
    }

}



int main() {
    srand(time(NULL));

    //ofstream("task1.txt");
    //ofstream("task2.txt");

    //task1();
    //cout << endl;
    task2();

}
