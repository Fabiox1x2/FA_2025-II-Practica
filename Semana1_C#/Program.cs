using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer5();
            Console.ReadKey();

        }
        static void ejer1()
        {
            string nombre, carrera; //declarando variables
            Console.WriteLine("ingrese su nomnbre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("ingrese su carrera: ");
            carrera = Console.ReadLine();
            Console.WriteLine($"\n{nombre}, bienvenido a FA de {carrera}");
        }
        static void ejer2()
        {
            Console.WriteLine("Ingrese numero x: ");
            int x = int.Parse(Console.ReadLine());
            Console.WriteLine("ingrese numero y: ");
            int y = int.Parse(Console.ReadLine());
            double resu = (double)x / (double)y;
            Console.WriteLine("Suma: " + (x + y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicacion: " + (x * y));
            Console.WriteLine("Division: " + resu);
        }
         
            static void ejer3()
            {
            
            }
            static void ejer4()
            {
             Console.WriteLine("ingerese un numero decimal");
             double num= Convert.ToDouble(Console.ReadLine());
             double raiz2= Math.Sqrt(num);
             int redo = (int)Math.Round(num, 0);
             double cubo= Math.Pow(num, 3);
             double raiz3 = Math.Pow(num, 1 / 3d);
             Console.WriteLine("Raiz 2: " + raiz2);
             Console.WriteLine("Redondeado: " + redo);
             Console.WriteLine("AL cubo: " + cubo);
             Console.WriteLine("Raiz3: " + raiz3);
            }
            static void ejer5()
            {
             Console.WriteLine("ingrese numero: ");
             string num = Console.ReadLine();
             int entero = int.Parse(num);
             double deci= double.Parse(num);

             Console.WriteLine("Resto: "+(entero%2));
             Console.WriteLine(
            }
            static void ejer6()
            {

            }
        }


    }

