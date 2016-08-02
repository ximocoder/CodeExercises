using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // http://www.forocoches.com/foro/showthread.php?p=235196945#post235196945

            System.Console.WriteLine("tonto quien lo lea");
            //    imprimir las edades de las personas cuyo nombre empiece por "P" 
            //    y que sean mayores de 19 años, ordenadas de forma descendiente 
            //    y multiplicadas por dos, y sin que en el resultado se muestren 
            //    los números 100 y 101.
            var foo = new Dictionary<string, int>()
            {
                { "Alejandro", 19 },
                { "Alejandro2", 20 },
                { "Pepe", 20 },
                { "Paco", 50 },
                { "Jorge", 30 },
                { "Jorge2", 50 },
                { "Jorge3", 30 },
                { "Porge", 30 },
                { "Porge2", 15 },
                { "Porge3", 35 },
                { "Porge4", 30 }
            };

            foo.Where(n => n.Key[0] == 'P' && n.Value > 19).Select(i => i.Value * 2).OrderByDescending(i => i).Except(new List<int> { 100, 101 }).ToList().ForEach(p => { Console.WriteLine(p.ToString()); });

            Console.ReadKey();

        }
    }
}
