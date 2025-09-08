def perceptron(x1,x2, w1,w2,theta):
    state = x1*w1 + x2*w2
    if(state >= theta):
        return 1
    else:
        return 0


x1 = int(input())
x2 = int(input())

# and gate
def AND(x1, x2):
    return perceptron(x1, x2, 1, 1, 1.2)
print('and: ' , AND(x1, x2))

# nand gate
def NAND(x1, x2):
    return perceptron(x1, x2, -1,-1,-1.2)
print('nand: ' , NAND(x1, x2))

# or gate
def OR(x1, x2):
    return perceptron(x1, x2, 2, 2, 1.2)
print('or: ' , perceptron(x1, x2, 2, 2, 1.2))

import numpy as np 

x = np.array([0,1])
w = np.array([0.5, 0.5])
b = - 0.7

aswr = np.sum(x*w) + b
print("and: " , aswr > 0)


def XOR(x1, x2):
    s_1 = NAND(x1, x2)
    s_2 = OR(x1, x2)
    return AND(s_1, s_2)

print("XOR: " ,XOR(x1,x2))