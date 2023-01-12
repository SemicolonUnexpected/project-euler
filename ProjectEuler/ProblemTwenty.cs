using ProjectEuler.Number;

namespace ProjectEuler {
    public class ProblemTwenty : IExecutable {
        public string Execute() {
            return $"The sum of the digits of 100 factorial is {Operations.DigitSum(Operations.Factorial(100))}";
        }
    }
}
