using System;
using System.Diagnostics;

namespace ProjectEuler {
    class Program {

        static readonly IExecutable problem = new ProblemTen();

        static Stopwatch stopwatch = new Stopwatch();

        static void Main(string[] args) {
            Console.WriteLine("----- Project Euler -----");
            Console.WriteLine("\nExecuting " + problem.ToString() + "\n");

            stopwatch.Start();

            Console.WriteLine(problem.Execute());

            stopwatch.Stop();

            DisplayTime();
        }

        public static void DisplayTime() {
            Console.WriteLine("\nExecution time was : " + stopwatch.ElapsedMilliseconds + " ms");
        }
    }
}
