from math import factorial
import sys
sys.setrecursionlimit(5000000)

def factS(arg):
    return factorial(int(arg))

"""
код этого класса скопирован из Интернет-источника чуть менее чем полностью,
но зато он позволяет вычислять большие числа фибоначчи намного быстрее, чем рекурсивный алгоритм
"""
class FIB:
    @staticmethod
    def Mpow(x, n, I, mult):
        """
        Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая 
        перемножается с mult, а n – положительное целое
        """
        if n == 0:
            return I
        elif n == 1:
            return x
        else:
            y = FIB.Mpow(x, n // 2, I, mult)
            y = mult(y, y)
            if n % 2:
                y = mult(x, y)
            return y
    
    @staticmethod
    def identity_matrix(n):
        """Возвращает единичную матрицу n на n"""
        r = list(range(n))
        return [[1 if i == j else 0 for i in r] for j in r]
    
    @staticmethod
    def matrix_multiply(A, B):
        BT = list(zip(*B))
        return [[sum(a * b
                     for a, b in zip(row_a, col_b))
                for col_b in BT]
                for row_a in A]
    
    @staticmethod
    def fib(arg):
        n = int(arg)
        F = FIB.Mpow([[1, 1], [1, 0]], n, FIB.identity_matrix(2), FIB.matrix_multiply)
        return F[0][1]
    
acahe = dict()

def ack(m,n):
    if (m,n) in acahe:
        return acahe[(m,n)]
    else:
        if (m==0):
            acahe[(m,n)] = n + 1
        elif (n==0):
            acahe[(m,n)] = ack(m-1,1)
        else:
            acahe[(m,n)] = ack(m-1,ack(m,n-1))
        return acahe[(m,n)]

def ackS(arg):
    m,n = list(map(lambda x: int(x), arg.split(sep=' ')))
    return ack(m,n)

#соответствия между аббревиатурами функций в исходном файле и функциями в программе
fmap = {'FIB':FIB.fib, 'F':factS, 'ACK':ackS}