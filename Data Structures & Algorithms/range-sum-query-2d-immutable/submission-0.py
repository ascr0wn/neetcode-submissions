class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1,y1,x2,y2 = row1, col1, row2, col2
        total_sum = 0
        while x1 <= x2:
            y1 = col1
            while y1 <= y2:
                total_sum += self.matrix[x1][y1]
                y1 += 1
            x1 += 1
        return total_sum        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)