using System;
using System.IO;
using System.Linq;

namespace ProjectEuler {
	class ProblemEleven : IExecutable {
		public string Execute() {
			int[,] grid = ReadInGrid();
			int[] maxSums = LargestSum(grid);
			return $"The largest sum of 4 numbers in the same direction in the following grid is {maxSums.Max()}" + DisplayGrid();

			//Returns the gird as a string
			static string DisplayGrid() {
				return "\n" + Properties.TextFiles.ProblemEleven;
            }
		}
		
		//Sets up the grid of integers
		int[,] ReadInGrid() {
			string[] lines = Properties.TextFiles.ProblemEleven.Split('\n');

            int[,] output = new int[20, 20];

            for (int i = 0; i < 20; i++) {
				int[] numbers = Array.ConvertAll<string, int>(lines[i].Split(" "), int.Parse);

				for (int j = 0; j < 20; j++) {
					output[i, j] = numbers[j];
                }
            }

			return output;
		}

		//Gets the largest sum of the 20 by 20 grid
		int[] LargestSum(int[,] grid) {
			int[] output = new int[4] { Horizontal(), Vertical(), DiagonalRight(), DiagonalLeft() };

			return output;

			int Horizontal() {
				int output = 0;
				int current;

				for (int i = 0; i < 20; i++) {
					for (int j = 0; j < 16; j++) {
						current = 1;
                        for (int k = 0; k < 4; k++) {
							current *= grid[i, j + k];
                        }
                        if (current > output) {
							output = current;
                        }
					}
				}

				return output;
			}

			int Vertical() {
				int output = 0;
				int current;

				for (int i = 0; i < 16; i++) {
					for (int j = 0; j < 20; j++) {
						current = 1;
						for (int k = 0; k < 4; k++) {
							current *= grid[i + k, j];
						}
						if (current > output) {
							output = current;
						}
					}
				}

				return output;
			}

			int DiagonalRight() {
				int output = 0;
				int current;

				for (int i = 0; i < 17; i++) {
					for (int j = 0; j < 17; j++) {
						current = 1;
						for (int k = 0; k < 4; k++) {
							current *= grid[i + k, j + k];
						}
						if (current > output) {
							output = current;
						}
					}
				}

				return output;
			}

			int DiagonalLeft() {
				int output = 0;
				int current;

				for (int i = 3; i < 20; i++) {
					for (int j = 0; j < 17; j++) {
						current = 1;
						for (int k = 0; k < 4; k++) {
							current *= grid[i - k, j + k];
						}
						if (current > output) {
							output = current;
						}
					}
				}

				return output;
			}
		}
	}
}