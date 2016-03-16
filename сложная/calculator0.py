from math import factorial
import sys
sys.setrecursionlimit(5000000)

def fib(n):
    if (n<2):
        return n
    else:
        return fib(n-2) + fib(n-1)

def fibS(arg):
    return fib(int(arg))

def factS(arg):
    return factorial(int(arg))
    
def ack(m,n):
    if (m==0):
        return n+1
    elif (n==0):
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))

def ackS(arg):
    m,n = list(map(lambda x: int(x), arg.split(sep=' ')))
    return ack(m,n)

#соответствия между аббревиатурами функций в исходном файле и функциями в программе
fmap = {'FIB':fibS, 'F':factS, 'ACK':ackS}