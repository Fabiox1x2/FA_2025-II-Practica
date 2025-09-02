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
            ejer2();
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
            double resu = x / y;
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

            }
            static void ejer5()
            {

            }
            static void ejer6()
            {

            }
        }


    }

