using System;
using System.Collections.Generic;
using ProjectEuler.Number;

namespace ProjectEuler {
	class ProblemTwelve : IExecutable {

		public string Execute() {
			return $"The first triangular number to have over  {GetFirstTriangularNumberWithFactors(500)}";
		}

        //Finds the first triangular number with a number of factors
        long GetFirstTriangularNumberWithFactors(int numberOfFactors) {
            List<long> primes = Primes.GetSieveOfEratosthenes(100000);
            var triangularNumbers = TriangularNumbers.GetTriangularNumbers();
            long output = 0;

            foreach (long number in triangularNumbers) {
                if (NumberOfFactors(number, primes) >= 500) {
                    output = number;
                    break;
                }
            }

            return output;
		}

        //Finds the number of factors of a number when a list of primes is provided
		int NumberOfFactors(long number, List<long> primes) {
            if (number == 1) {
                return 1;
            }

			int numberOfFactors = 1;
			
            int i = 0;
            while (number > 1) {
                int exponent = 1;

                while (number % primes[i] == 0) {
                    number /= primes[i];
                    exponent++;
                }

                if (primes[i] > number) {
                    numberOfFactors *= 2;
                    break;
                }

                numberOfFactors *= exponent;
                i++;
            }

			return numberOfFactors;
        }
	}
}
