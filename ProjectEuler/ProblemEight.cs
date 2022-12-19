using System;
using System.IO;

namespace ProjectEuler {
    class ProblemEight : IExecutable {

        const string PATH = @"TextFiles\ProblemEight.txt";

        public string Execute() {
            int[] digits = ToIntArray(ReadIn());
            return $"The largest product of 13 consecutive digits in the following 1000 digit number is {MaxProduct(digits, 13)}\n\n{ReadIn()}";
        }

        //Gets the string of digits from the file and removes new lines
        string ReadIn() {
            using StreamReader streamReader = new StreamReader(PATH);
            return streamReader.ReadToEnd().Replace(Environment.NewLine, String.Empty);
        }

        //Converts a string of digits to an array of digits
        int[] ToIntArray(string value) {
            char[] characters = value.ToCharArray();
            int[] digits = Array.ConvertAll(characters, c => (int)Char.GetNumericValue(c));
            return digits;
        }

        //Finds the max product of a number of consecutive digits in an array of digits
        long MaxProduct(int[] digits, int numberOfDigitsToSum) {
            long largestSum = 0;

            for (int i = 0; i < digits.Length - numberOfDigitsToSum; i++) {
                long sum = 1;

                for (int j = 0; j < numberOfDigitsToSum; j++) {
                    sum *= digits[i + j];
                }

                if (sum > largestSum) {
                    largestSum = sum;
                }     
            }
            return largestSum;
        }
    }
}