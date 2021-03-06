import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split


# 通过计算斜率和截距画拟合直线
def draw_line(model, color):
    k = model.coef_
    b = model.intercept_
    line = k * x_data + b
    plt.plot(x_data, line, color, 50)
    plt.scatter(x_data, y_data, c='r')
    plt.show()


if __name__ == '__main__':
    x_data = np.random.randint(0, 100, 80, int)
    noise = np.random.normal(0, 5, x_data.shape)
    y_data = x_data * 3 + 2 + noise
    x_data = x_data.reshape(-1, 1)
    y_data = y_data.reshape(-1, 1)

    plt.scatter(x_data, y_data)
    plt.show()

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)

    # 线性回归
    lr_model = LinearRegression()
    lr_model.fit(x_train, y_train)
    lr_prediction = lr_model.predict(x_test)
    print('线性回归准确率:', lr_model.score(x_test, y_test))

    # 岭回归
    rd_model = Ridge()
    rd_model.fit(x_train, y_train)
    rd_prediction = rd_model.predict(x_test)
    print('岭回归准确率:', rd_model.score(x_test, y_test))

    # 套索回归
    ls_model = Lasso()
    ls_model.fit(x_train, y_train)
    ls_prediction = ls_model.predict(x_test)
    print('套索回归准确率:', ls_model.score(x_test, y_test))

    draw_line(lr_model, 'b')
    draw_line(rd_model, 'y')
    draw_line(ls_model, 'g')

