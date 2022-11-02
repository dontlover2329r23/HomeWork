using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Matrix
{
    internal class Matr
    {
        private int m;
        private int n;
        private double[,] matr;
        public int N { get { return n; } set { N = value; } }
        public int M { get { return m; } set { M = value; } }
        public double[,] Matrix { get { return matr; } set { matr = value; } }
        public bool IsSquare { get => this.M == this.N; }
        public Matr(int n = 0, int m = 0, bool Zero = false)
        {
            this.m = m;
            this.n = n;
            Random r = new Random();
            Random d = new Random();
            double[,] matr = new double[n, m];
            if (Zero)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        matr[i, j] = 0;
                    }
                }
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        matr[i, j] = r.Next(10);
                    }
                }
            }
            this.matr = matr;
        }
        public Matr(Matr m)
        {
            this.n = m.n;
            this.m = m.m;
            this.matr = m.matr;
        }
        public Matr()
        {
            Console.WriteLine("Введите размерность матрицы (Все значения вводить с новой строки): ");

            n = Convert.ToInt32(Console.ReadLine());

            m = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Введите матрицу: ");
            double[,] matr = new double[n, n];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    matr[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
            this.Matrix = matr;
        }
        // Вывод матрицы с клавиатуры
        public void ReadMat()
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.Write(matr[i, j] + "\t");
                }
                Console.WriteLine();
            }
        }
        // Умножение матрицы А на число
        public static Matr umnch(Matr a, int ch)
        {
            
            for (int i = 0; i < a.N; i++)
            {
                for (int j = 0; j < a.M; j++)
                {
                     a.matr[i, j] = a.matr[i, j] * ch;
                }
            }
            return a;
        }
        // Деление матрицы А на число
        public static Matr Division(Matr a, int ch)
        {
            
            for (int i = 0; i < a.N; i++)
            {
                for (int j = 0; j < a.M; j++)
                {
                    a.matr[i, j] = a.matr[i, j] / ch;
                }
            }
            return a;
        }

        // Умножение матрицы А на матрицу Б
        public static void Umn(Matr a, Matr b)
        {
            if (a.M == b.N)
            {
                Matr resMass = new Matr(a.N, b.M,true);
                for (int i = 0; i < a.N; i++)
                    for (int j = 0; j < b.M; j++)
                        for (int k = 0; k < b.M; k++)
                            resMass.matr[i, j] += a.matr[i, k] * b.matr[k, j];



                resMass.ReadMat();
            }
            else
            {
                Console.WriteLine("не совпадают размерности");
            }
        }
        public static Matr operator *(Matr a, int b)
        {
            return Matr.umnch(a, b);
        }
        public static Matr operator /(Matr a, int b)
        {
            return Matr.Division(a, b);
        }

        // Метод вычитания матриц
        public static void razn(Matr a, Matr b)
        {
            if ((a.N == b.M) && (a.M == b.N))
            {
                Matr resMass = new Matr(a.N, a.M,true);
                for (int i = 0; i < a.N; i++)
                {
                    for (int j = 0; j < b.M; j++)
                    {
                        resMass.matr[i, j] = a.matr[i, j] - b.matr[i, j];
                    }
                }
                resMass.ReadMat();
            }
            else { Console.WriteLine("не совпадают размерности"); }

        }
        //Сумма матриц
        public static void Sum(Matr a, Matr b)
        { 
            if ((a.N == b.M) && (a.M == b.N))
            {
                Matr resMass = new Matr(a.N, a.M,true);
                for (int i = 0; i < a.N; i++)
                {
                    for (int j = 0; j < b.M; j++)
                    {
                        resMass.matr[i, j] = a.matr[i, j] + b.matr[i, j];
                    }
                }
                resMass.ReadMat();
            }
            else { Console.WriteLine("не совпадают размерности"); }
        }

        //Транспонирование матрицы
        public static Matr transposition(Matr a)
        {



            Matr resMass = new Matr(a.N, a.M,true);
            for (int i = 0; i < a.N; i++)
                for (int j = 0; j < a.M; j++)
                {
                    if (i == j)
                    {
                        resMass.matr[i, j] = a.matr[i, j];
                    }
                    else
                    {
                        resMass.matr[j, i] = a.matr[i, j];
                    }

                }
            return resMass;
        }
        //Вывод конкретного элемента
        public static double output_of_an_element(Matr a,int i,int j)
        {
            if ((i > -1) && (j > -1) && (i < a.N) && (j < a.M))
            {
                
                return a.matr[i, j];
            }
            else
            {
                Console.WriteLine("Нет такого элемента в матрице");
                return -1;
            }
        }
    }
}
