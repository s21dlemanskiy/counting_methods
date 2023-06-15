import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self):
        self.w = None

    @staticmethod
    def mse(y_true: 'np.array(n, )', y_pred: 'np.array(n, )'):
        return np.mean((y_true - y_pred) ** 2)

    @staticmethod
    def x_type_correction(X):
        if str(type(X)) == "<class 'pandas.core.frame.DataFrame'>":
            X = X.to_numpy(dtype=np.double)
        elif str(type(X)) == "<class 'pandas.core.series.Series'>":
            X = pd.DataFrame(X).to_numpy(dtype=np.double)
        elif str(type(X)) == "<class 'list'>":
            if str(type(X[0])) == "<class 'list'>":
                X = np.array(X, dtype=np.double)
            else:
                X = np.array(tuple(map(lambda x: [x], X)), dtype=np.double)
        elif str(type(X)) == "<class 'numpy.ndarray'>":
            pass
        else:
            print('unsupported type')
            raise ValueError
        if not np.isrealobj(X.dtype):
            print(f'unsupported type of values: {X.dtype}')
            raise ValueError
        return X

    @staticmethod
    def y_type_correction(y):
        if str(type(y)) == "<class 'pandas.core.frame.DataFrame'>":
            print(f'unsupported type of y {type(y)}')
            raise ValueError
            # y = y.to_numpy(dtype=np.double)
        elif str(type(y)) == "<class 'pandas.core.series.Series'>":
            y = y.to_numpy(dtype=np.double)
        elif str(type(y)) == "<class 'list'>":
            if str(type(y[0])) == "<class 'list'>":
                print('unsupported type of y(list of lists)')
                raise ValueError
            y = np.array(y, dtype=np.double)
        elif str(type(y)) == "<class 'numpy.ndarray'>":
            pass
        else:
            print('unsupported type')
            raise ValueError
        if not np.isrealobj(y.dtype):
            print(f'unsupported type of values: {y.dtype}')
            raise ValueError
        assert len(y.shape) == 1, f"strange y shape: {y.shape}"
        return y

    def fit(self, X, y, epsilon=0.01, batchsize=1):
        rd = np.random.RandomState(42)
        X = self.x_type_correction(X)
        y = self.y_type_correction(y)
        assert X.shape[0] == y.shape[0], f"not equal shapes X:{X.shape} not equal to y:{y.shape}"
        if self.w is None or self.w.shape[0] != y.shape[0]:
            self.w = np.ones(X.shape[1])
        iteration = 0
        while iteration < 10 ** 6:
            rows = rd.choice(X.shape[0], size=batchsize, replace=False)
            batch_x = X[rows, :]
            batch_y = y[rows]
            difference = np.mean(batch_x.dot(self.w) - batch_y)
            grad = (2 * difference) * (np.mean(batch_x, axis=0))
            cur_mse = self.mse(batch_x.dot(self.w), batch_y)
            sub_iter = 0
            while self.mse(batch_x.dot(self.w - grad), batch_y) >= cur_mse:
                grad = grad / 2
                sub_iter += 1
                if sub_iter > 100:
                    break
            else:
                self.w = self.w - grad
                if np.max(np.abs(difference)) < epsilon:
                    break
                iteration += 1
        print(f"done for {iteration} iterations")

    def predict(self, X):
        X = self.x_type_correction(X)
        # print(X.shape[1])
        assert self.w.shape[0] == X.shape[1]
        return X.dot(self.w)
