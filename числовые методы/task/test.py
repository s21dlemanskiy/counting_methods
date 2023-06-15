from interpolation.inter_net_func import *
from interpolation.ploting import plot_result

from interpolation.linear_regression import LinearRegression

from sklearn.datasets import make_regression

from sklearn import linear_model

# x_arr = [1, 2, 5, 10]
# y_arr = [2, 4, -7, 2]
# plot_result(x_arr, y_arr, LagrangeExpr(x_arr, y_arr))
#
# x_arr = [1, 2, 5, 7,  10]
# y_arr = [2, 4, -7, 10,  2]
# plot_result(x_arr, y_arr, LagrangeExpr(x_arr, y_arr))

# x_arr = [2, 3, 5, 1]
# y_arr = [3, 5, 7, 5]
#
# ne = NutonExpr(x_list=x_arr, y_list=y_arr)
# plot_result(x_arr, y_arr, ne)
# ne = NutonExpr()
# for x, y in zip(x_arr, y_arr):
#     ne.add_point(x, y)
# plot_result(x_arr, y_arr, ne)

#
lr = LinearRegression()
x = [1, 2, 3, 4]
y = [5, 6, 8, 10]
x_with_one = list(map(lambda var_x: [var_x, 1], x))
lr.fit(x_with_one, y, batchsize=1)
plot_result(x, y, lambda x_1: lr.predict([[x_1, 1]]))

lr = LinearRegression()
x, y = make_regression(n_samples=100, n_features=1, noise=50, random_state=42)
x_with_one = list(map(lambda var_x: [var_x[0], 1], x))
lr.fit(x_with_one, y, batchsize=10)
plot_result(x, y, lambda x_1: lr.predict([[x_1, 1]]))

lm = linear_model.LinearRegression()
lm.fit(x, y)
print(x)
plot_result(x, y, lambda x_1: lm.predict([[x_1]]))

