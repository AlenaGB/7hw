class Matrix:
    def __init__(self, list1, list2):
        # self.matr = [list1, list2]
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list1)):

            for j in range(len(self.list2[i])):
                matr[i][j] = self.list1[i][j] + self.list2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())