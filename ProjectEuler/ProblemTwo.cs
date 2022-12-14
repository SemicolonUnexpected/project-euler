using ProjectEuler.Number;

namespace ProjectEuler {
    class ProblemTwo : IExecutable {

        public string Execute() {
            return $"The sum of all fibonacci numbers below 4,000,000 is  + {SumOfFibonaccis(4000000)}";
        }
        
        //Finds the sum of all even fibanacci numbers less than a number
        long SumOfFibonaccis(long upperBound) {
            var fibonacciNumbers = FibonacciNumbers.GetFibonacciNumbers();
            long output = 0;

            foreach (long fibonacciNumber in fibonacciNumbers) {
                if (fibonacciNumber % 2 == 0) {
                    output += fibonacciNumber;
                }

                if (fibonacciNumber > upperBound) break;
            }

            return output;
        }
        
    }
}
