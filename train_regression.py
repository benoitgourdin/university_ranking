from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split


def regression(X, y_data):

    # define train and test data
    X_train, X_test, y_train, y_test = train_test_split(DataFrame(X), DataFrame(y_data), test_size=0.1, random_state=0)

    # regression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # get score
    y_pred = regressor.predict(X_test)
    score = 1 - mean_absolute_error(y_pred, y_test)
    print("score of the algorithm: " + str(score))

    return regressor

