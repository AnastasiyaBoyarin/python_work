class Matrix:
    def __init__(self, i_list):
        self.i_list = i_list

    def print_matrix(self):
        for el in self.i_list:
            print(el)

    def __str__(self):
        new_string = ''
        for el in self.i_list:
            new_string += str(el) + '\n'
        return new_string

    def __add__(self, other):
        if len(self.i_list) != len(other.i_list):
            exit('Error. Sum of two matrix is not possible')
        res_finish = []
        for i in range(len(self.i_list)):
            res_list = []
            for j in range(len(self.i_list[i])):
                res_list.append(self.i_list[i][j] + other.i_list[i][j])
            res_finish.append(res_list)
        result_obj = Matrix(res_finish)
        return result_obj


array_1 = [[31, 22, 5], [37, 43, 8], [51, 86, 12], [657, 54, 5], [5, 5, 4]]
array_2 = [[3, 4, 9], [37, 8, 12], [51, 876, 1], [65, -5, 5], [5, 55, 4]]

matrix1 = Matrix(array_1)
matrix2 = Matrix(array_2)

print(matrix1.i_list, '\n')
print(matrix2.i_list, '\n')
matrix1.print_matrix()
print()
print(matrix1)
matrix2.print_matrix()
print()
print(matrix2)

matrix_sum = matrix1 + matrix2
print(f'Sum of two matrix: \n{matrix_sum}')
