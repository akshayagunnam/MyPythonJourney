"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            pascal = [[1], [1, 1]]
            for i in range(numRows - 2):
                L = len(pascal[-1])
                lst = []
                for j in range(L - 1):
                    lst.append(pascal[-1][j] + pascal[-1][j + 1])
                pascal.append([1] + lst + [1])
            return pascal
