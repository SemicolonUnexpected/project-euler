using System;
using System.Collections.Generic;
using System.Numerics;
using System.Text;

namespace ProjectEuler.Number {
    static class Operations {

        /// <summary>
        /// Finds the sum of the digits of a number
        /// </summary>
        /// <param name="number"></param>
        /// <returns></returns>
        public static BigInteger DigitSum(BigInteger number) {
            BigInteger output = 0;

            while (number > 0) {
                output += number % 10;
                number /= 10;
            }

            return output;
        }

        public static BigInteger Factorial(int number) {
            BigInteger output = 1;

            for (int i = number; i >= 1; i--) {
                output *= i;
            }

            return output;
        }
    }
}
