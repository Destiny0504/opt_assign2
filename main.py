import Q1
import Q2
import Q3

def main():
    Q1.goldsearch(Q1.obj_function, -2, 2, 1e-5, 'max')
    Q1.Dichotomous(Q1.obj_function, -2, 2, 1e-2, 1e-5, 'max')
    Q2.cyclic(
        Q2.obj_function,
        init_X = [-4, -5], # -2.5, 2
        x_bound = [[-5, 5], [-5, 5]],
        tol = 1e-50
    )
    Q3.powell(
        Q3.obj_function,
        init_X = [-4, -5], # -2.5, 2
        x_bound = [[-5, 5], [-5, 5]],
        tol = 1e-7
    )

if __name__=="__main__":
    main()