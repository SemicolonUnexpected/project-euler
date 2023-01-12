using System;
using System.Diagnostics;

namespace ProjectEuler {
    class Program {

        static readonly IExecutable problem = new ProblemEighteen();

        static readonly Stopwatch stopwatch = new Stopwatch();

        static void Main() {
            Console.WriteLine("----- Project Euler -----");

            ExecuteProblem(problem);
        }

        private static void ExecuteProblem(IExecutable problem) {
            Console.WriteLine("\nExecuting " + problem.ToString() + "\n");

            stopwatch.Start();

            string output = problem.Execute();

            stopwatch.Stop();

            Console.WriteLine(output);

            DisplayTime();
        }

        public static void DisplayTime() {
            Console.WriteLine("\nExecution time was : " + stopwatch.ElapsedMilliseconds + " ms");
        }
    }
}
