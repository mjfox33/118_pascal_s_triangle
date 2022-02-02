class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = list()
        for i in range(numRows):
            row = list()
            for j in range(i+1):
                cell = 1 if j==0 or j == i else result[i-1][j-1]+result[i-1][j]
                row.append(cell)
            result.append(row)
        return result
# f(i,j) = 1 if j=0 or j=row_number
# f(i,j) = f(i-1,j-1) + f(i-1,j)


test = [1, 5]
s = Solution()
r1 = s.generate(test[0])
r2 = s.generate(test[1])
print(r1)
print(r2)