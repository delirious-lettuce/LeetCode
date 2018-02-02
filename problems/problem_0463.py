class Solution:
    """
    https://leetcode.com/problems/island-perimeter/

    You are given a map in form of a two-dimensional integer grid where
      1 represents land and 0 represents water. Grid cells are
      connected horizontally/vertically (not diagonally). The grid is
      completely surrounded by water, and there is exactly one island
      (i.e., one or more connected land cells). The island doesn't have
      "lakes" (water inside that isn't connected to the water around
      the island). One cell is a square with side length 1. The grid is
      rectangular, width and height don't exceed 100. Determine the
      perimeter of the island.

    Example:

      [[0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0]]

      Answer: 16
    """

    @staticmethod
    def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        result = 0
        width = len(grid[0])
        for x in range(len(grid)):
            for y in range(width):
                if grid[x][y]:
                    result += 4
                    if x > 0 and grid[x - 1][y]:
                        result -= 2
                    if y > 0 and grid[x][y - 1]:
                        result -= 2
        return result
