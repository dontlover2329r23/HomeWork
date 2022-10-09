namespace ConsoleApp1
{
    internal class coordinates
    {
        double x;
        double y;
        double z;

        public coordinates(double X, double Y, double Z)
        {
            this.x = X;
            this.y = Y;
            this.z = Z;
        }

        public void show()
        {
            Console.WriteLine("{0},{1},{2}", this.x, this.y, this.z);
        }

        public static double distance1(coordinates a, coordinates b)
        {
            double dist;
            dist = Math.Sqrt(Math.Pow(a.x - b.x, 2) + Math.Pow(a.y - b.y, 2) + Math.Pow(a.z - b.z, 2));
            return dist;
        }

        public static void the_equation1(coordinates a, coordinates b)
        {
            Console.WriteLine("(x-{0})/{1}=(y-{2})/{3}=(z-{4})/{5}", a.x, b.x - a.x, a.y, b.y - a.y, a.z, b.z - a.z);
        }
        public static void the_equation2(coordinates a, coordinates b, coordinates c)
        {
            Console.WriteLine("(x-{0})*{1}-( у-{2})*{3}+( z-{4})*{5} = 0", a.x, (b.y - a.y) * (c.z - a.z) - (c.y - a.y) * (b.z - a.z), a.y, (b.x - a.x) * (c.z - a.z) - (b.z - a.z) * (c.x - a.x), a.z, (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x));
        }
        public static double distance2(coordinates a)
        {
            double dist;
            dist = Math.Sqrt(Math.Pow(a.x, 2) + Math.Pow(a.y, 2) + Math.Pow(a.z, 2));
            return dist;
        }

        public static coordinates operator_plus(coordinates a, coordinates b)
        {
            return new(a.x + b.x, a.y + b.y, a.z + b.z);
        }

        public static double operator_multiplication1(coordinates a, coordinates b)
        {
            return a.x * b.x + a.y * b.y + a.z * b.z;
        }
        public static void operator_multiplication2(coordinates a, coordinates b)
        {
            Console.WriteLine("{0}*i - ({1})*j + ({2})*k", a.y * b.z - a.z * b.y, a.x * b.z - a.z * b.x, a.x * b.y - a.y * b.x);
        }
    }


}
