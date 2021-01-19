from keras.layers import Input, Dense, Flatten
from keras.models import Model, Sequential
from sklearn.model_selection import KFold, cross_val_score
import numpy as np
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ann(X, y_data):

    # ann
    model = MLPRegressor(hidden_layer_sizes=3, activation='relu', solver='adam', batch_size='auto', max_iter=200)

    X_train, X_test, y_train, y_test = train_test_split(DataFrame(X), DataFrame(y_data), test_size=0.1, random_state=0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print("score of the algorithm: " + str(score))

    return model