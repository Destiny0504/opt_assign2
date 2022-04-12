import numpy as np
import matplotlib.pyplot as plt

def obj_function(x: list):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2


def goldSearch(func, d, cur_pos, min_b, max_b, tol):
    R = (3 - 5**0.5) / 2
    x1 = min_b + (max_b - min_b) * R
    x2 = min_b + max_b - x1

    # print(cur_pos)

    f1 = func(cur_pos + x1 * d)
    f2 = func(cur_pos + x2 * d)

    while max_b - min_b > tol:
        if f1 < f2:
            max_b, x2, f2 = x2, x1, f1
            x1 = min_b + R * (max_b - min_b)
            f1 = func(cur_pos + x1 * d)
            min_x = x1
        else:
            min_b, x1, f1 = x1, x2, f2
            x2 = max_b - R * (max_b - min_b)
            f2 = func(cur_pos + x2 * d)
            min_x = x2

    return {'X': min_x, 'y': func(cur_pos + min_x * d)}


def powell(func, init_X, x_bound, tol):
    dim = 2 # The objective function has two variables
    d = np.eye(dim) #identity
    new_x = None

    min_x_list = [init_X]
    while new_x is None or np.max(np.abs(init_X - new_x)) > tol:
        cur_pos = init_X

        for i in range(dim):
            # print(d[:, i])
            result = goldSearch(
                func = func,
                d = d[:, i],
                cur_pos = cur_pos,
                min_b = x_bound[i][0] - cur_pos[0],
                max_b = x_bound[i][1] - cur_pos[1],
                tol=tol
            )
            lmb = result['X']
            cur_pos = cur_pos + lmb * d[:, i]
            min_x_list.append(cur_pos)

        for i in range(dim - 1):
            d[:, i] = d[:, i + 1]
        d[:, dim - 1] = cur_pos - init_X
        # normalization
        d[:, dim - 1] = d[:, dim - 1] / np.linalg.norm(d[:, dim - 1], ord=2)

        new_x = init_X
        result = goldSearch(
            func = func,
            d = d[:, dim - 1],
            cur_pos = cur_pos,
            min_b = x_bound[dim - 1][0] - cur_pos[0],
            max_b = x_bound[dim - 1][1] - cur_pos[1],
            tol=tol
        )
        lmb = result['X']
        init_X = cur_pos + lmb * d[:, dim - 1]
        min_x_list.append(init_X)
    min_y = func(init_X)

    # print(min_x)
    # print([x[0] for x in min_x_list])
    # print([x[1] for x in min_x_list])
    # print(min_y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot([x[0] for x in min_x_list], [x[1] for x in min_x_list])
    plt.savefig(f'./result/powell.png', format = "png")
    plt.clf()
    return {'X': init_X, 'y': min_y, 'x_list': min_x_list}
