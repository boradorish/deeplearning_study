import numpy as np
import matplotlib.pylab as plt

def step_function_stashed(x):
    if (x>0):
        return 1
    else:
        return 0

def step_function(x):
    y = x > 0
    return y.astype(int)

x = np.array([-1.0, 1.2, 0.9])
print("step function with np array:", step_function(x))

x2 = np.arange(-5.0, 5.0, 0.1)
def draw(y):
    plt.plot(x2,y)
    plt.ylim(-0.1,1.1)
    plt.show()
    
# draw step function
y = step_function(x2)
# draw(y)

def sigmoid(x):
    return 1/ (1+ np.exp(-x))

print("sigmoid:", sigmoid(x))

# draw sigmoid function
y2 = sigmoid(x2)
# draw(y2)

def relu(x):
    return np.maximum(0,x)

print("relu: ", relu(x))
#draw relu function
y3 = relu(x2)
draw(y3)