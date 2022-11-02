using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
 
namespace Matrix
{
    internal class RevMatr : SquareMatr
    {
        //Является ли матрица обратимой
        public bool IsInv
        {
            get
            {
                if (this.M == this.N && Determinant() != 0)
                {
                    return true;
                }
                else { return false; }
            }
        }
        public RevMatr(SquareMatr m) : base(m)
        {
 
        }
 
        //находим обратную матрицу
        public Matr Inv()
        {
            var determinant = Determinant();
 
            Matr result = new Matr(M, M, true);
            if (!this.IsInv)
            {
                throw new InvalidOperationException("Matrix not inversible!");
            }
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < M; j++)
                {
                    result.Matrix[i, j] = ((i + j) % 2 == 1 ? -1 : 1) * CalculateMinor(i, j) / determinant;
                }
            }
            result = transposition(result);
 
            return result;
        }
        //Считаем миноры
        private double CalculateMinor(int i, int j)
        {
            return this.deleting_a_column_and_row(i, j).Determinant();
        }
 
 
    }
}
