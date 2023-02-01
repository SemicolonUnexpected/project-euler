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

		/// <summary>
		/// Finds the factors of all integers within a given range
		/// </summary>
		/// <param name="upperBound"></param>
		/// <returns></returns>
		/// <exception cref="ArgumentOutOfRangeException"></exception>
		public static List<long>[] GetFactors(long upperBound) {
            if (upperBound <= 1) {
                throw new ArgumentOutOfRangeException();
            }

			List<long>[] factors = new List<long>[upperBound];

			for (int i = 0; i < factors.Length; i++) {
				factors[i] = new List<long>();
            }

			for (int i = 0; i <= upperBound; i++) {
				for (int j = 0; j <= upperBound - i - 1; j += i + 1) {
					factors[i + j].Add(i + 1);
				}
			}

			return factors;
        }

		/// <summary>
		/// Finds the sum of the proper divisors for all numbers less than the upper bound
		/// </summary>
		/// <param name="upperBound"></param>
		/// <returns></returns>
		/// <exception cref="ArgumentOutOfRangeException"></exception>
		// O(n * (ln(n) + 0.577)
		public static long[] GetSumProperDivisors(long upperBound) {
			if (upperBound <= 1) {
				throw new ArgumentOutOfRangeException();
			}

			long[] sumProperDivisors = new long[upperBound];

			for (int i = 1; i < sumProperDivisors.Length; i++) {
				for (int j = i; j + i < sumProperDivisors.Length; j += i) {
					sumProperDivisors[i + j] += i;
				}
			}

			return sumProperDivisors;
        }
	}
}
