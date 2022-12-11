using System;
using System.Collections.Generic;
using System.Text;

namespace ProjectEuler.Number {
    static class TriangularNumbers {
		/// <summary>
		/// Gives all triangular numbers by adding prevoius terms
		/// </summary>
		/// <returns></returns>
		public static IEnumerable<long> GetTriangularNumbers() {
			long triangularNumber = 0;
			long i = 0;

			while (true) {
				i++;
				triangularNumber += i;
				yield return triangularNumber;
			}
		}
	}
}
