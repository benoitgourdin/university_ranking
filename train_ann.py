from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.neural_network import MLPRegressor


def ann(X, y_data):

    # ann
    model = MLPRegressor(hidden_layer_sizes=(), activation='relu', solver='adam', batch_size=1, max_iter=150)

    X_train, X_test, y_train, y_test = train_test_split(DataFrame(X), DataFrame(y_data), test_size=0.1, random_state=0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = 1 - mean_absolute_error(y_pred, y_test)
    print("score of the algorithm: " + str(score))

    return model
