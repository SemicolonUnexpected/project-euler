using System.Collections.Generic;
using System.Linq;

namespace ProjectEuler {
	class ProblemFourteen : IExecutable {

		public string Execute() {
			return $"The starting number, under one million, which produces the longest chain in the Collatz conjecture is {MaxCollatz(1000000)}";
		}

        //Finds the starting number under an upper bound that produces the longest chain before terminating
        long MaxCollatz(long upperBound) {
            Dictionary<long, long> collatzLengths = new Dictionary<long, long>();
            collatzLengths.Add(1, 1);

            long maxLength = 0;
            long maxLengthBase = 0;

            //If you can double the value and stay within the range, double the value will produce a longer chain
            for (long i = upperBound / 2; i < upperBound + 1; i++) {
                if (CollatzLength(i) > maxLength) {
                    maxLength = CollatzLength(i);
                    maxLengthBase = i;
                }
            }

            return maxLengthBase;

            //Finds the length of the chain recursively, avoiding recalculations with the help the collatzLengths dictionary
            long CollatzLength(long number) {
                if (collatzLengths.ContainsKey(number)) {
                    return collatzLengths[number];
                }
                else if (number % 2 == 0) {
                    number /= 2;
                    return CollatzLength(number) + 1;
                }
                else {
                    number *= 3;
                    number++;
                    number /= 2;
                    return CollatzLength(number) + 2;
                }
            }
        }
    }
}
