using System; 
using System.Collections.Generic; 
using System.Diagnostics; 
using System.Linq; 
using System.Text; 
using System.Threading.Tasks; 
 
namespace Matrix 
{
 internal class SquareMatr : Matr 
    {
 
 
 public SquareMatr(Matr m) : base(m) 
        {
 
 
        }
 //Удаление столбца и строки 
 public SquareMatr deleting_a_column_and_row(int k, int d) 
        {
 Matr a = new Matr(this.N - 1, this.N - 1, true); 
 SquareMatr b = new SquareMatr(a); 
 
 for (int i = 0; i < N; i++) 
            {
 for (int j = 0; j < N; j++) 
                {
 if (i < k && j < d) 
                    {
 b.Matrix[i, j] = Matrix[i, j]; 
                    }
 else if (i < k && j > d) 
                    {
 b.Matrix[i, j - 1] = Matrix[i, j]; 
                    }
 else if (i > k && j < d) 
                    {
 b.Matrix[i - 1, j] = Matrix[i, j]; 
                    }
 else if (i > k && j > d) 
                    {
 b.Matrix[i - 1, j - 1] = Matrix[i, j]; 
                    }
                }
            }
 return b; 
        }
 //Определитель матрицы 
 double deter = 0; 
 public double Determinant() 
        {
 
 if (!this.IsSquare) 
            {
 throw new InvalidOperationException("Определителя нет,так как матрица не квадратичная"); 
            }
 if (this.N == 1) 
            {
 return Matrix[0, 0]; 
            }
 if (this.M == 2) 
            {
                return this.Matrix[0, 0] * this.Matrix[1, 1] - this.Matrix[1, 0] * this.Matrix[0, 1];
            }
            for (int j = 0; j < N; j++)
            {
                deter += Math.Pow((-1), j) * Matrix[0, j] * deleting_a_column_and_row(0, j).Determinant();
            }
 
            return deter;
        }
    }
}
