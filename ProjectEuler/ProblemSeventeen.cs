using System;

namespace ProjectEuler {
    class ProblemSeventeen : IExecutable {

        public string Execute() {
            string letters = "";

            for (int i = 1; i < 1001; i++) {
                letters += NumberToWords(i);
            }

            letters = letters.Replace(" ", "");
            letters = letters.Replace("-", "");

            return $"{letters.Length}";
        }

        //Converts a positive integer to words
        private string NumberToWords(int number) {
            string output = "";
            string[] toNineteen = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".Split(" ");
            string[] tens = "twenty thirty forty fifty sixty seventy eighty ninety".Split(" ");

            if (number >= 1000000000) {
                output += NumberToWords(number / 1000000000) + " billion";
                number %= 1000000000;
            }

            if (number >= 1000000) {
                output += NumberToWords(number / 1000000) + " million";
                number %= 1000000;
            }


            if (number >= 1000) {
                output += NumberToWords(number / 1000) + " thousand";
                number %= 1000;
            }

            if (number >= 100) {
                output += toNineteen[number / 100 - 1] + " hundred";
                number %= 100;
            }

            if (number >= 20) {
                if (output != "") {
                    output += " and";
                }

                output += " " + tens[number / 10 - 2];
                number %= 10;

                if (number > 0) {
                    output += "-" + toNineteen[number - 1];
                }
            }
            else if(number > 0) {
                if (output != "") {
                    output += " and";
                }

                output += " " + toNineteen[number - 1];
            }
            else if (output == "") {
                return "zero";
            }

            return output.TrimStart();
        }
    }
}