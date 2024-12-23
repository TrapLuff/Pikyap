using System;

namespace lab2 {

    abstract class Figure{
        public abstract double Area();

        public override string ToString()
    {
        return Area().ToString();
    }
    }

    interface IPrint
    {
        void Print();
    }

    class Rectangle: Figure, IPrint {
        public double Width;
        public double Height;

        public Rectangle(double width, double height)
        {
            Width = width;
            Height = height;
        }
        public override double Area()
        {
            return Width * Height;
        }
        public override string ToString()
        {
            return "Характеристики прямоугольника".PadRight(30) + "[Ширина: " + Width + ", Высота: " + Height + ", Площадь: " + Area() + "]";
        }
        public void Print()
        {
            Console.WriteLine(ToString());
        }

    }

    class Square: Rectangle, IPrint {
        public Square(double side) : base(side, side)
        {}

        public override string ToString()
        {
            return "Характеристики квадрата".PadRight(30) + "[Сторона: " + Width + ", Площадь: " + Area() + "]";
        }

    }

    class Circle: Figure, IPrint {
        public double Radius;
        public Circle(double radius)
        {
            Radius = radius;
        }
        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }
        public override string ToString()
        {
            return "Характеристики круга".PadRight(30) + "[Радиус: " + Radius + ", Площадь: " + Area() + "]";
        }
            public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
    class Program{
        static void Main() {
            Rectangle rectangle = new Rectangle(5, 10);
            Square square = new Square(7);
            Circle circle = new Circle(3.5);

            rectangle.Print();
            square.Print();
            circle.Print();
        }
    
    }
}