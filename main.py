import Q1

if __name__=="__main__":
    Q1.goldsearch(Q1.obj_function, -2, 2, 1e-5, 'max')
    Q1.Dichotomous(Q1.obj_function, -2, 2, 1e-2, 1e-5, 'max')