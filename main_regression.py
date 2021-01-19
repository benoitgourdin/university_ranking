import csv

from sklearn.preprocessing import StandardScaler

from prepare_input import prepare_input
from preparing_score_ranking import prepare_score_ranking
from train_regression import regression
from preparing_data import prepare_data

if __name__ == '__main__':

    X_columns = ['female ratio', 'teaching score', 'international score', 'research score', 'citations', 'income',
                 'student/staff ratio', 'international students', 'number of students']
    X = [30, 95, 95, 75, 70, 70, 0.8, 30, 20000]

    score_ranking_filename = 'score_ranking_2015.csv'
    data_filename = 'times_data_2011_15.csv'
    score_ranking_names = ['ranking', 'score']
    data_names = ['female ratio', 'teaching score', 'international score', 'research score', 'citations', 'income',
                  'total score', 'student/staff ratio', 'international students', 'number of students']

    #import score_ranking
    raw_data = open(score_ranking_filename, 'rt')
    reader = csv.reader(raw_data, delimiter=';', quoting=csv.QUOTE_NONE)
    score_ranking = list(reader)

    #import data
    raw_data_2 = open(data_filename, 'rt')
    reader_2 = csv.reader(raw_data_2, delimiter=';', quoting=csv.QUOTE_NONE)
    data = list(reader_2)

    #preparation
    X_data, y_data, scaler = prepare_data(data)
    score_ranking = prepare_score_ranking(score_ranking)
    #Standardize
    standardScaler = StandardScaler()
    standardScaler.fit(X_data)
    x = standardScaler.transform(X_data)

    #regression
    model = regression(x, y_data)

    #preparation
    X_prepared = prepare_input(X, scaler)
    #Standardize
    x = standardScaler.transform([X_prepared])

    y = model.predict(x)
    for k in score_ranking:
        if y == k[1]:
            rank = k[0]
            break
        elif y > k[1]:
            rank = k[0] - 1
            break
    print("projected rank: " + str(rank))
    print("score: " + str(y[0]))