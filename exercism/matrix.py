### Exercise - 5 - MATRIX

class Matrix:
    def __init__(self, matrix_string):
        listy = matrix_string.split('\n')
        self.mat = []
        for i in listy:
            data = i.split()
            conv = []
            for x in data:
                conv.append(int(x))
            self.mat.append(conv)

    def row(self, index):
        alpha = index - 1
        return self.mat[alpha]

    def column(self, index):
        j = 0
        p = []
        col = []
        while j < len(self.mat[0]):
            for i in range(len(self.mat)):
                p.append(self.mat[i][j])
            col.append(p)
            p = []
            j += 1
        beta = index - 1
        return col[beta]