using System;
using System.Numerics;
using System.IO;

namespace ProjectEuler {
    class ProblemThirteen : IExecutable {
        public string Execute() {
            BigInteger[] numbers = ReadInFirstElevenDigits();
            BigInteger sum = 0;

            foreach (var num in numbers) {
                sum += num;
            }

            return "The first ten digits of the sum of the one hundred fifty digit numbers is " + sum.ToString().Substring(0, 10);
        }

        //Reads in the first eleven digits of the numbers from the file
        BigInteger[] ReadInFirstElevenDigits() {
            string[] lines = Properties.TextFiles.ProblemThirteen.Split('\n');

            for (int i = 0; i < lines.Length; i++) {
                lines[i] = lines[i].Substring(0, 11);
            }

            return Array.ConvertAll<string, BigInteger>(lines, BigInteger.Parse);
        }
    }
}
