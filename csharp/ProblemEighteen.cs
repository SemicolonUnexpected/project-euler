using System;

namespace ProjectEuler {
    class ProblemEighteen : IExecutable {
        public string Execute() {
            return $"The maximum sum that can be made in the following pyramid by travelling only down or down and right is {GetMaximumPathSum()}\n{Properties.TextFiles.ProblemEighteen}";
        }

        //Finds the maximum path by going through the triangle from the last row to the first, adding the larger of the two numbers to the number above
        int GetMaximumPathSum() {
            int[][] grid = SetUpTriangularGrid();

            for (int i = grid.Length - 2; i >= 0; i--) {
                for (int j = 0; j < grid[i].Length; j++) {
                    //Add the greater of the two numbers below 
                    grid[i][j] += Math.Max(grid[i + 1][j], grid[i + 1][j + 1]);
                }
            }

            return grid[0][0];
        }

        //Converts the text file into a jagged array representation of the triangle
        int[][] SetUpTriangularGrid() {
            string[] lines = Properties.TextFiles.ProblemEighteen.Split("\n");
            int[][] grid = new int[lines.Length][];

            for (int i = 0; i < lines.Length; i++) {
                string[] numbersText = lines[i].Split(" ");
                int[] numbers = Array.ConvertAll<string, int>(numbersText, int.Parse);
                grid[i] = numbers;
            }

            return grid;
        }

    }
}