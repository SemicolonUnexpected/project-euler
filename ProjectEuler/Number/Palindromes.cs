using System;
using System.Collections.Generic;

namespace ProjectEuler.Number {
    static class Palindromes {
		/// <summary>
		/// Gives all four digit palindromic numbers in descending order
		/// </summary>
		/// <returns></returns>
		public static IEnumerable<int> GetFourDigitPalindromesDescending() {
			for (int i = 999; i > 99; i--) {
				int number = i;
				int reverse = 0;
				int palindrome = i * 1000;

				for (int j = 0; j < 3; j++) {

					reverse *= 10;
					reverse += number % 10;
					number /= 10;

				}
				yield return palindrome + reverse;
			}
		}
	}
}
