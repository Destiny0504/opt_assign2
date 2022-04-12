import copy
import numpy as np
import matplotlib.pyplot as plt
import random


def Euclidean_dist(v1, v2):
    return sum([(x1 - x2)**2 for x1, x2 in zip(v1, v2)])**0.5


def obj_function(x: list):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2


def goldSearch(func, a, b, tol):
    R = (5**0.5 - 1) / 2
    C = 1 - R

    x1 = R * a + C * b
    x2 = C * a + R * b
    y1 = func(x1)
    y2 = func(x2)

    while (b - a) > tol:
        if y1 > y2:
            a, x1, y1 = x1, x2, y2
            x2 = C * a + R * b
            y2 = func(x2)
        else:
            b, x2, y2 = x2, x1, y1
            x1 = R * a + C * b
            y1 = func(x1)

    if y1 < y2:
        min_y = y1
        min_x = x1
    else:
        min_y = y2
        min_x = x2
    return min_y, min_x


def cyclic(func, init_X, x_bound, tol):
    min_x = init_X

    min_x_list = [min_x]
    while True:
        record_min_y = []
        record_min_x = []
        for index, x_i in enumerate(min_x):
            temp_x = copy.deepcopy(min_x)

            def gold_func(x):
                temp_x[index] = x
                return func(temp_x)

            ret_y, ret_x = goldSearch(
                func=gold_func,
                a = x_bound[index][0],
                b = x_bound[index][1],
                tol=1e-5
            )
            temp_x[index] = ret_x
            record_min_y.append(ret_y)
            record_min_x.append(temp_x)
        new_x = record_min_x[record_min_y.index(min(record_min_y))]
        if Euclidean_dist(new_x, min_x) < tol:
            min_x = new_x
            break
        min_x = new_x
        min_x_list.append(min_x)
    # print(min_x)
    # print([x[0] for x in min_x_list])
    # print([x[1] for x in min_x_list])
    # print(func(min_x))
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot([x[0] for x in min_x_list], [x[1] for x in min_x_list])
    plt.savefig(f'./result/cyclic_{len(min_x_list)}.png', format = "png")
    plt.clf()
    return {'y': func(min_x), 'X': min_x, 'x_list': min_x_list}


if __name__ == "__main__":
    result = cyclic(x_bound_list=[[-2, 2], [-2, 2]], tol=1e-4)
    print(f"(x, y): {result['X']}, f(x, y): {result['y']}")