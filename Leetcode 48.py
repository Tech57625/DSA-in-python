class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Tranpose

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # swap 2: Reverse avery row
        for i in range(n):
            matrix[i].reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
obj.rotate(matrix)

print(matrix)