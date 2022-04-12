import math
import matplotlib.pyplot as plt
import numpy as np

def obj_function(x, type : str = 'min'):
    if type == 'min':
        return round(x**3 * math.exp(-x**2), 8)
    else :
        return round(-(x**3 * math.exp(-x**2)), 8)

def goldsearch(f, a, b, tol, type : str = 'min'):
    '''
        f : object function
        a : lower bound
        b : upper bound
        tol : tolerance
        type : find minimum or maximum
    '''
    count = 0
    golden_ratio = (math.sqrt(5) - 1) / 2
    step = []
    value = []

    C = 1 - golden_ratio

    x1 = golden_ratio * a + C * b
    x2 = C * a + golden_ratio * b

    while abs(b - a) > tol:
        count += 1
        if f(x1, type) > f(x2, type):
            value.append(f(x1, 'min'))
            step.append(count)
            a, x1= x1, x2
            x2 = C * a + golden_ratio * b
        else:
            value.append(f(x2, 'min'))
            step.append(count)
            b, x2 = x2, x1
            x1 = golden_ratio * a + C * b

    step.append(count + 1)
    print(count)
    plt.xlabel('step')
    plt.ylabel('value')
    if f(x1, type) < f(x2, type):
        value.append(f(x1, 'min'))
        print(x1)
        print(f'Steps : {step}')
        plt.scatter(step, value)
        plt.xticks(np.arange(1, count + 2, 2))
        plt.savefig('./result/Q1.png', format = "png")
        plt.clf()
        return x1
    else :
        value.append(f(x2, 'min'))
        print(x2)
        print(f'Steps : {step}')
        plt.scatter(step, value)
        plt.xticks(np.arange(1, count + 2, 2))
        plt.savefig(f'./result/golden_search_{type}.png', format = "png")
        plt.clf()
        return x2

def Dichotomous(f, a, b, ep, tol, type : str = 'min'):
    count = 0
    value = []
    while abs(f(b, type) - f(a, type)) > tol:
        mid = (a + b) / 2

        if f(mid - ep, type) < f(mid + ep, type):
            b = mid + ep
        else:
            a = mid - ep
        count += 1
        value.append(f(mid, 'min'))
        print(f(mid, 'min'))
    mid = (a + b) / 2
    value.append(f(mid, 'min'))

    plt.xlabel('step')
    plt.ylabel('value')
    plt.scatter(np.arange(1, count + 2, 1), value)
    plt.xticks(np.arange(1, count + 2, 2))
    plt.savefig(f'./result/Dichotomous_{type}.png', format = "png")
    plt.clf()


if __name__=="__main__":
    goldsearch(obj_function, -2, 2, 1e-5)