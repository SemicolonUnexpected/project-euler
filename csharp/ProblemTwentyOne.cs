using ProjectEuler.Number;
using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler {
    internal class ProblemTwentyOne : IExecutable {
        public string Execute() {
            string output = "";
            List<long> amicableNumbers = GetAmicableNumbers();

            foreach (var item in amicableNumbers) {
                output += item + " ";
            }
            return $"The amicable numbers under 10,000 are... \n{output}\nTheir sum is {amicableNumbers.Sum()}";
        }

        List<long> GetAmicableNumbers() {
            long[] sumOfProperDivisors = Primes.GetSumProperDivisors(10001);
            List<long> output = new List<long>();

            for (int i = 0; i < sumOfProperDivisors.Length; i++) {
                if (sumOfProperDivisors[i] < sumOfProperDivisors.Length - 1 && i != sumOfProperDivisors[i] && i == sumOfProperDivisors[sumOfProperDivisors[i]]) {
                    output.Add(i);
                }
            }

            return output;
        }
    }
}