using System.Collections.Generic;
using System.Linq;
using ProjectEuler.Number;

namespace ProjectEuler {
	class ProblemTen : IExecutable {

		public string Execute() {
			List<long> primes = Primes.GetSieveOfEratosthenes(2000000);
			return $"The sum of all the primes that are below 2000000 is {primes.Sum()}";
		}
	}
}