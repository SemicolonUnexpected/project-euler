using System.Numerics;
using ProjectEuler.Number;

namespace ProjectEuler {
    class ProblemSixteen : IExecutable {
        public string Execute() {
            return $"The sum of the digits of 2^1000 is {Operations.DigitSum(BigInteger.Pow(2, 1000))}";
        }
    }
}
