using System;
using System.Collections.Generic;

namespace ProjectEuler.Number {
    static class FibonacciNumbers {
		/// <summary>
		/// Gives fibonacci numbers
		/// </summary>
		/// <returns></returns>
		public static IEnumerable<long> GetFibonacciNumbers() {
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
}
