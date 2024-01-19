using System.Collections.Generic;
using ProjectEuler.Number;

namespace ProjectEuler {
    class ProblemFour : IExecutable {
        public string Execute() {
            return $"The largest palindrome made from the product of two 3-digit numbers is {GetLargestThreeDigitDivisorPalindrome()}";
        }

        //Returns the largest palindrome with two three digit divisors
        private int GetLargestThreeDigitDivisorPalindrome() {
            List<int> palindromes = new List<int>(Palindromes.GetSixDigitPalindromesDescending());
            int output = 0;

            foreach (int palindrome in palindromes) {
                if (HasThreeDigitDivisors(palindrome)) {
                    output = palindrome;
                    break;
                }
            }

            return output;
        }

        //Checks if a number has two three digit divisors
        private bool HasThreeDigitDivisors(int value) {

            for (int i = 100; i * i < value; i++) {
                if (value % i == 0 && value / i < 1000) {
                    return true;
                }
            }

            return false;
        }
    }
}
