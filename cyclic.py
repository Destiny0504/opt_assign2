import copy
import matplotlib as plt
import random

def E_dist(v1, v2):
    return sum([(x1 - x2)**2 for x1, x2 in zip(v1, v2)])**0.5


def f(x: list):
    return (4 - 2.1 * x[0]**2 + (x[0]**4) / 3) * x[0]**2 + x[0] * x[1] + (-4 + 4 * x[1]**2) * x[1]**2


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


def cyclic(func, init_X, x_bound_list, tol):
    min_x = init_X
    # for lb, rb in x_bound_list:
    #     min_x.append((lb + rb) / 2 + 1)

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
                a=x_bound_list[index][0],
                b=x_bound_list[index][1],
                tol=1e-5
            )
            temp_x[index] = ret_x
            record_min_y.append(ret_y)
            record_min_x.append(temp_x)
        new_x = record_min_x[record_min_y.index(min(record_min_y))]
        if E_dist(new_x, min_x) < tol:
            min_x = new_x
            break
        min_x = new_x
        min_x_list.append(min_x)
    return {'y': func(min_x), 'X': min_x, 'x_list': min_x_list}


if __name__ == "__main__":
    result = cyclic(x_bound_list=[[-2, 2], [-2, 2]], tol=1e-4)
    print(f"(x, y): {result['X']}, f(x, y): {result['y']}")