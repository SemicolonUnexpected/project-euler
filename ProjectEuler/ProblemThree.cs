using System.Collections.Generic;
using System;
using ProjectEuler.Number;

namespace ProjectEuler {
    class ProblemThree : IExecutable {

        public string Execute() {
            return $"The largest prime factor of 600851475143 is {LargestPrimeFactor(600851475143)}";
        }

        //Finds the largest prime factor of a number
        long LargestPrimeFactor(long number) {

            long largestPrimeFactor = number;
            List<long> primes = Primes.GetSieveOfEratosthenes((long)Math.Sqrt(number));

            foreach (long prime in primes) {
                while (number % prime == 0) {
                    number /= prime;
                    largestPrimeFactor = prime;
                }

                if (number == 1) {
                    break;
                }
            }

            return largestPrimeFactor;
        }
    }
}
