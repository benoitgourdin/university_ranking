from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score


def regression(X, y_data):

    # define train and test data
    cv = KFold(n_splits=10, random_state=1, shuffle=True)

    # regression
    regressor = LinearRegression()
    scores = cross_val_score(regressor, X, y_data, cv=cv)

    # get score
    score = scores.mean()
    print("score of the algorithm: " + str(score))

    # train algorithm
    regressor.fit(X, y_data)
    return regressor

