#3 б)
class Matrix:
  def __init__(self, data):
    self.data = data

  def __str__(self):
    matrix_str = ""
    for row in self.data:
      for element in row:
        matrix_str += str(element) + " "
      matrix_str += "\n"
    return matrix_str
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1)