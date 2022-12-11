using System;
using System.Collections.Generic;

namespace ProjectEuler.Number {
    static class Primes {
		/// <summary>
		/// Gives all the primes below a certain number by producing a sieve of Eratosthenes. Upper bounds must be greater than one
		/// </summary>
		/// <param name="upperBound"></param>
		/// <returns></returns>
		public static List<long> GetSieveOfEratosthenes(long upperBound) {
            if (upperBound <= 1) {
				throw new ArgumentOutOfRangeException();
            }

			long realBounds = (upperBound / 2) - 1;
			List<long> output = new List<long>();
			bool[] sieve = new bool[realBounds];
			Array.Fill<bool>(sieve, true);

			output.Add(2);

			for (int i = 0; i < realBounds; i++) {
				if (sieve[i]) {
					long realValue = 2 * i + 3;
					output.Add(realValue);
					for (long j = i + realValue; j < realBounds; j += realValue) {
						sieve[j] = false;
					}
				}

			}

			return output;
		}

		/// <summary>
		/// Checks if a number is prime by trial division
		/// </summary>
		/// <param name="value"></param>
		/// <returns></returns>
		public static bool IsPrime(long value) {
			for (long i = 3; i * i <= value; i += 2) {
				if (value % i == 0) return false;
			}

			return true;
		}
	}
}
