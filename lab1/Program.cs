using System;

namespace lab2 {

    class Program {

        static void Main() {
            Console.BackgroundColor = ConsoleColor.Black;
            double A = 0, B = 0, C = 0;
            
            A = GetDoubleValue("Введите значение A: ");
            B = GetDoubleValue("Введите значение B: ");
            C = GetDoubleValue("Введите значение C: ");

            List<double> Roots = GetRoots(A, B, C);

            Console.WriteLine("Значения введены: A = {0}, B = {1}, C = {2}", A, B, C);

            if (Roots.Count == 0){
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Корней не существует");
            }
            else if (Roots.Count == 1){
                Console.Write("Существует один корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[0]);

            }
            else if (Roots.Count == 2){
                Console.Write("Существует два корня \nПервый корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[0]);
                Console.ResetColor();
                Console.Write("Второй корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[1]);
            }
            else if (Roots.Count == 4){
                Console.Write("Существует четыре корня \nПервый корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[0]);
                Console.ResetColor();
                Console.Write("Второй корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[1]);
                Console.ResetColor();
                Console.Write("Третий корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[2]);
                Console.ResetColor();
                Console.Write("Четвертый корень: ");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(Roots[3]);
            }
        Console.ResetColor();
        }

        static double GetDoubleValue(string msg) {
            double value;
            while (true) {
                Console.Write(msg);
                var input = Console.ReadLine();
                
                if (double.TryParse(input, out value)) {
                    return value;
                } else {
                    Console.WriteLine("Некорректное значение. Попробуйте еще раз.");
                }
            }
        }

        static List<double> GetRoots(double A, double B, double C){
            List<double> Roots = new List<double>();
            double D = B*B - 4*A*C;
            if (D == 0.0){
                double Root = -B/(2.0*A);
                if (Root == 0){
                    Roots.Add(Math.Abs(Root));
                }
                else if (Root > 0){
                    Roots.Add(Math.Sqrt(Root));
                    Roots.Add(-Math.Sqrt(Root));
                }
            }
            else if (D > 0){    
                double Sqd = Math.Sqrt(D);
                double Root1 = (-B + Sqd) / (2.0*A);
                double Root2 = (-B - Sqd) / (2.0*A);
                if (Root1 == 0){
                    Roots.Add(Math.Abs(Root1));
                }
                else if (Root1 > 0){
                    Roots.Add(Math.Sqrt(Root1));
                    Roots.Add(-Math.Sqrt(Root1));
                }
                if (Root2 == 0){
                    Roots.Add(Math.Abs(Root2));
                }
                else if (Root2 > 0){
                    Roots.Add(Math.Sqrt(Root2));
                    Roots.Add(-Math.Sqrt(Root2));
                }
            }
            return Roots;
        }
    }
}