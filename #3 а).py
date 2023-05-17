#3 а)
class Matrix:
    def __init__(self, data):
        self.matrix = data
    
    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(str(e) for e in row))

m1 = Matrix([[1,2,3], [4,5,6]])
m1.print_matrix()