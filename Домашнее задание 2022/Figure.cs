using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp5
{
    class figure : coordinates
    {
        private coordinates A;
        private coordinates B;
        private coordinates C;
        private coordinates D;

        public figure(coordinates a, coordinates b, coordinates c, coordinates d)
        {
            this.A = a;
            this.B = b;
            this.C = c;
            this.D = d;
        }
        public static bool points_lie_in_the_same_plane(figure F)
        {
            double k = (F.D.X - F.A.X) * ((F.B.Y - F.A.Y) * (F.C.Z - F.A.Z) - (F.C.Y - F.A.Y) * (F.B.Z - F.A.Z)) - (F.D.Y - F.A.Y) * ((F.B.X - F.A.X) * (F.C.Z - F.A.Z) - (F.B.Z - F.A.Z) * (F.C.X - F.A.X)) + (F.D.Z - F.A.Z) * ((F.B.X - F.A.X) * (F.C.Y - F.A.Y) - (F.B.Y - F.A.Y) * (F.C.X - F.A.X));
            if (k == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        public static double the_area_of_the_figure(figure F)
        {
            if (points_lie_in_the_same_plane(F))
            {
                double S = (coordinates.distance1(F.A, F.B) + coordinates.distance1(F.B, F.C) + coordinates.distance1(F.C, F.D) + coordinates.distance1(F.D, F.A)) / 2;
                return Math.Sqrt((S - coordinates.distance1(F.A, F.B)) * (S - coordinates.distance1(F.B, F.C)) * (S - coordinates.distance1(F.C, F.D)) * (S - coordinates.distance1(F.D, F.A)));
            }
            else
            {
                return -1;
            }
        }
        public static double the_perimeter_of_the_figure(figure F)
        {
            if (points_lie_in_the_same_plane(F))
            {
                return coordinates.distance1(F.A, F.B) + coordinates.distance1(F.B, F.C) + coordinates.distance1(F.C, F.D) + coordinates.distance1(F.D, F.A);
            }
            else
            {
                return -1;
            }
        }
        public static void diagonal_lengths(figure F)
        {
            Console.WriteLine("AC = {0}, BD = {1}", coordinates.distance1(F.A, F.C), coordinates.distance1(F.B, F.D));
        }
        public static void convex_figure_or_not(figure F)
        {
            coordinates AB = new coordinates(F.A.X - F.B.X, F.A.Y - F.B.Y);
            coordinates BC = new coordinates(F.B.X - F.C.X, F.B.Y - F.C.Y);
            coordinates CD = new coordinates(F.C.X - F.D.X, F.C.Y - F.D.Y);
            coordinates DA = new coordinates(F.D.X - F.A.X, F.D.Y - F.A.Y);
            double ab = AB.X * BC.Y - AB.Y * BC.X;
            double bc = BC.X * CD.Y - BC.Y * CD.X;
            double cd = CD.X * DA.Y - CD.Y * DA.X;
            if (points_lie_in_the_same_plane(F))
            {
                if ((Math.Sign(ab) == Math.Sign(cd)) && (Math.Sign(cd) == Math.Sign(bc)))
                {
                    Console.WriteLine("Выпуклый");
                }
                else
                {
                    Console.WriteLine("Вогнутый");
                }
            }
            else
            {
                Console.WriteLine("Точки лежат в разных плоскостях");
            }
        }
        public static void WHAT_KIND_OF_FIGURES(figure F)
        {
            coordinates AB = new coordinates(F.A.X - F.B.X, F.A.Y - F.B.Y);
            coordinates BC = new coordinates(F.B.X - F.C.X, F.B.Y - F.C.Y);
            coordinates CD = new coordinates(F.C.X - F.D.X, F.C.Y - F.D.Y);
            coordinates DA = new coordinates(F.D.X - F.A.X, F.D.Y - F.A.Y);
            double ab = coordinates.distance1(F.A, F.B);
            double bc = coordinates.distance1(F.B, F.C);
            double cd = coordinates.distance1(F.C, F.D);
            double da = coordinates.distance1(F.D, F.A);
            double abbc = Math.Acos((AB.X * BC.X + AB.Y * BC.Y) / Math.Sqrt(AB.X * AB.X + AB.Y * AB.Y) / Math.Sqrt(BC.X * BC.X + BC.Y * BC.Y));
            double abcd = Math.Acos((AB.X * CD.X + AB.Y * CD.Y) / Math.Sqrt(AB.X * AB.X + AB.Y * AB.Y) / Math.Sqrt(CD.X * CD.X + CD.Y * CD.Y));
            double bcda = Math.Acos((BC.X * DA.X + BC.Y * DA.Y) / Math.Sqrt(BC.X * BC.X + BC.Y * BC.Y) / Math.Sqrt(DA.X * DA.X + DA.Y * DA.Y));
            if ((ab == bc) && (bc == cd) && (cd == da))
            {
                if (abbc == Math.PI / 2)
                {
                    Console.WriteLine("Квадрат");
                }
                else
                {
                    Console.WriteLine("Ромб");
                }
            }
            else if ((ab == cd) && (bc == da))
            {
                if (abbc == Math.PI / 2)
                {
                    Console.WriteLine("Прямоугольник");
                }
                else
                {
                    Console.WriteLine("Параллелограмм");
                }
            }
            else if (abcd == Math.PI || bcda == Math.PI)
            {
                Console.WriteLine("Трапеция");
            }
            else
            {
                convex_figure_or_not(F);
            }
        }

    }
}
