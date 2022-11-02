using Matrix; 
 
Console.WriteLine("Рандомная матрица А:"); 
Matr a = new Matr(3, 3); 
a.ReadMat(); 
Matr c = new Matr(3, 3); 
Console.WriteLine(); 
 
Console.WriteLine("Рандомная матрица Б:"); 
Matr b = new Matr(3, 3); 
b.ReadMat(); 
 
Console.WriteLine(); 
 
Console.WriteLine("Сумма А и Б:"); 
 Matr.Sum(a,b); 
 
 
Console.WriteLine(); 
 
Console.WriteLine("Умножение А на Б: "); 
Matr.Umn(a, b); 
 
Console.WriteLine();
 
Console.WriteLine("Деление А на 2:");
c = Matr.Division(a, 2);
c.ReadMat();
Console.WriteLine();
Console.WriteLine("Умножение  А на 3:");
c = Matr.umnch(a, 3);
c.ReadMat();
Console.WriteLine();
Console.WriteLine("Вычитание матриц: ");
Matr.razn(a, b);
Console.WriteLine();
Console.WriteLine("Транспонирование матрицы А: ");
c = Matr.transposition(a);
c.ReadMat();
Console.WriteLine();
Console.WriteLine("Вывод конкретного элемент:а ");
Console.WriteLine("Введите строку ");
int i = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите столбец ");
int j = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Элемент:"+Matr.output_of_an_element(a,i,j));
Console.WriteLine();
SquareMatr A = new SquareMatr(a);
Console.WriteLine("Определитель матрицы А:", A.Determinant());
RevMatr D = new RevMatr(A);
 
Console.WriteLine();
 
A.ReadMat(); ;
 
Console.WriteLine();
Console.WriteLine("Обратная матрице А");
D.Inv().ReadMat(); 
