class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # In the Pascals's Triangle, i'th row has i number of elements
        # with both extremes of that row having value as 1.
        # Now we can find out the value at j'th index (not an extreme) as following:
        # currentRow[j] = lastRow[j - 1] + lastRow[j]
        output = []
        for i in range(1, numRows + 1):
            current = []
            for j in range(i):
                if((j == 0) or (j == (i - 1))):
                    current.append(1)
                else:
                    current.append(output[-1][j - 1] + output[-1][j])
            output.append(current)
        return output