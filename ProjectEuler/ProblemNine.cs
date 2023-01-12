using System;
using System.Linq;

namespace ProjectEuler {

	class ProblemNine : IExecutable {
		public string Execute() {
			int[] primitiveTriple = TripletThatSumsTo(1000);

			if (primitiveTriple is null) return "There is no pythagorean triple that sums to 1000";

			int tripletSum = primitiveTriple.Sum();
			int scaleDifference = 1000 / tripletSum;
			int[] actualTriple = new int[3] { primitiveTriple[0] * scaleDifference, primitiveTriple[1] * scaleDifference, primitiveTriple[2] * scaleDifference };

			return $"The pythagorean triplet of which a + b + c = 1000 is ({actualTriple[0]}, {actualTriple[1]}, {actualTriple[2]})\nProduct abc is {actualTriple[0] * actualTriple[1] * actualTriple[2]}";
        }

		//returns a pythagorean triplet for values of m and n
		int[] PythagoreanTriplet(int m, int n) {
			if (m < n || n < 1) throw new ArgumentOutOfRangeException("m must be greater than n and n must be greater than or equal to 1");

			return new int[3] { (2 * m * n), (m * m - n * n), (m * m + n * n)};
        }

		//Finds a pythagorean triplet that sums to a number
		int[] TripletThatSumsTo(int value) {
			int maxLoop = (int)Math.Floor(Math.Sqrt(value)) / 2;

            for (int m = 2; m < maxLoop; m++) {
                for (int n = 1; n < (m - 1); n++) {
					int[] triple = PythagoreanTriplet(m, n);

					if (value % triple.Sum() == 0) return PythagoreanTriplet(m, n);
                }
            }

			return null;
        }
	}
}
