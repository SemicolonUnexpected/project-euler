using System.Numerics;

namespace ProjectEuler {
    class ProblemSixteen : IExecutable {
        public string Execute() {
            return $"The sum of the digits of 2^1000 is {DigitSum(BigInteger.Pow(2, 1000))}";
        }

        //Finds the sum of the digits of a number
        private int DigitSum(BigInteger number) {
            int output = 0;

            while (number > 0) {
                output += (int)(number % 10);
                number /= 10;
            }

            return output;
        }
    }
}
