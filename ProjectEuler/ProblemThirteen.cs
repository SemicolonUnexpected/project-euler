using System;
using System.Numerics;
using System.IO;

namespace ProjectEuler {
	class ProblemThirteen : IExecutable {

		const string PATH = @"TextFiles\ProblemThirteen.txt";

		public string Execute() {
			BigInteger[] numbers = ReadInFirstElevenDigits();
			BigInteger sum = 0;
            foreach (var num in numbers) {
				sum += num;
            }
			return "The first ten digits of the sum of the one hundred fifty digit numbers is " + sum.ToString().Substring(0, 10);
		}

		BigInteger[] ReadInFirstElevenDigits() {
			string[] lines = File.ReadAllLines(PATH);

            for (int i = 0; i < lines.Length; i++) {
				lines[i] = lines[i].Substring(0, 11);
            }

			return  Array.ConvertAll<string, BigInteger>(lines, BigInteger.Parse);
        }
	}
}
