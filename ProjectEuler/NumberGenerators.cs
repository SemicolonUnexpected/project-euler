using System;
using System.Collections.Generic;

public static class NumberGenerators
{
	public static IEnumerable<long> GetPrimes() {
		yield return 2;

		long test = 3;
		while (true) {
			if (IsPrime(test)) yield return test;
			test += 2;
		}

		bool IsPrime(long value) {
			for (long i = 3; i <= Math.Sqrt(value); i += 2) {
				if (value % i == 0) return false;
			}

			return true;
		}
	}

	public static IEnumerable<long> TriangularNumbers() {
		long triangularNumber = 0;
		long i = 0;

		while (true) {
			i++;
			triangularNumber += i;
			yield return triangularNumber;
		}
	}
	public static IEnumerable<long> FibonacciNumbers() {
		long firstNumber = 0;
		long secondNumber = 1;
		long result;
		
		while (true) {
			result = firstNumber + secondNumber;
			yield return result;
			firstNumber = secondNumber;
			secondNumber = result;
		}
	}
}
