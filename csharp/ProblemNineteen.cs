using System;

namespace ProjectEuler {
    internal class ProblemNineteen : IExecutable {
        public string Execute() {
            return $"The number of months starting with a sunday in the 20th century is {NumberOfSundays(1901, 2000)}";
        }

        //Calculates the number of sundays using System.DateTime.DayOfTheWeek. Very Lazy!
        private int NumberOfSundays(int startyear, int endYear) {
            int number = 0;

            for (int i = startyear; i <= endYear; i++) {
                for (int j = 1; j <= 12; j++) {
                    DateTime date = new DateTime(i, j, 1);

                    if (date.DayOfWeek == 0) {
                        number++;
                    }
                }
            }

            return number;
        }
    }
}
