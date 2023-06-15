from sympy import *
import copy


class LagrangeExpr:
    def __init__(self, x_arr, y_arr):
        self.x = symbols('x', real=True)
        self.sympy_expr = sympify(0)
        self.create_expretion(x_arr, y_arr)

    def create_expretion(self, x_arr, y_arr):
        assert len(x_arr) == len(y_arr)
        for i in range(len(x_arr)):
            expr = sympify(1)
            for j in range(len(x_arr)):
                if i == j:
                    continue
                # print(f'expr * (x - {x_arr[j]}) / ({x_arr[i]} - {x_arr[j]})')
                expr = expr * (self.x - x_arr[j]) / (x_arr[i] - x_arr[j])
            self.sympy_expr += expr * y_arr[i]
        # print(latex(self.sympy_expr))

    def __call__(self, *args, **kwargs):
        assert self.sympy_expr is not None
        func = lambdify(self.x, self.sympy_expr)
        return func(*args, **kwargs)


class NutonExpr:
    def __init__(self, x_list=None, y_list=None):
        self.x = symbols('x', real=True)
        if x_list is not None and y_list is not None:
            self.add_points(x_list, y_list)
            return
        self.x_list = []
        self.y_list = []
        self.sympy_expr = None

    def add_points(self, x_list, y_list):
        assert len(x_list) == len(y_list)
        assert len(x_list) == len(set(x_list)), "x_list mast contain only unique values"
        a_list = []
        entity_list = list(map(sympify, y_list))
        shift = 1
        length = len(entity_list)
        while length - shift > 0:
            a_list += [entity_list[0]]
            for i in range(length - shift):
                entity_list[i] = (entity_list[i + 1] - entity_list[i]) / (x_list[i + shift] - x_list[i])
            shift += 1
        a_list += [entity_list[0]]
        production = 1
        self.sympy_expr = sympify(0)
        for i in range(len(a_list)):
            node = Mul(a_list[i], production, evaluate=False)
            self.sympy_expr += node
            production *= (self.x - x_list[i])
        self.x_list = copy.copy(x_list)
        self.y_list = copy.copy(y_list)

    def __call__(self, *args, **kwargs):
        assert self.sympy_expr is not None
        func = lambdify(self.x, self.sympy_expr)
        return func(*args, **kwargs)

    def add_point(self, x: float, y: float):
        if self.sympy_expr is None:
            self.sympy_expr = sympify(y)
            self.x_list += [x]
            self.y_list += [y]
            return
        production = 1
        for x_i in self.x_list:
            production *= (self.x - x_i)
        a_new = (y - self.sympy_expr) / production
        print(a_new)
        a_new = a_new.subs(self.x, x)
        node = Mul(a_new, production, evaluate=False)
        self.sympy_expr += node
        self.x_list += [x]
        self.y_list += [y]

    def latex(self):
        assert self.sympy_expr is not None
        return latex(self.sympy_expr)

    def __str__(self):
        assert self.sympy_expr is not None
        return str(self.sympy_expr)






