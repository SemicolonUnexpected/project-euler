using System.Linq;
using System.Collections.Generic;
using ProjectEuler.Number;

namespace ProjectEuler {
    class ProblemSeven : IExecutable {
		public string Execute() {
			List<long> primes = Primes.GetSieveOfEratosthenes(10001);
			return $"The 10,001st prime is " + primes[primes.Count() - 1];
		}
	}
}
