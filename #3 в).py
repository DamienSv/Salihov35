#3 в)
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result = [[0 for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        else:
            raise ValueError("Matrices must be of the same size")
m1 = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[6,5,4],[3,2,1]])
m3 = m1 + m2
for row in m3.matrix:
    print(" ".join(str(x) for x in row))