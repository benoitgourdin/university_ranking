import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def prepare_data(data):

    #delete date column
    [i.pop(0) for i in data]

    #delete column's names
    del data[0]

    # european to standard number format
    to_delete = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "":
                to_delete.append(i - len(to_delete))
                break
            data[i][j] = float(data[i][j].replace(",", "."))

    #delete rows with empty attributes
    for k in to_delete:
        del data[k]

    #scale percentage columns in data
    for m in range(len(data)):
        data[m][0] = data[m][0] / 100
        data[m][1] = data[m][1] / 100
        data[m][2] = data[m][2] / 100
        data[m][3] = data[m][3] / 100
        data[m][4] = data[m][4] / 100
        data[m][5] = data[m][5] / 100
        data[m][6] = data[m][6] / 100
        data[m][8] = data[m][8] / 100

    #scale students amount
    number_students_list = []
    scaler = MinMaxScaler()
    for row in data:
        number_students_list.append(row[7])
        row.pop(7)
    number_students = pd.DataFrame(number_students_list)
    scaled_number_students = list(scaler.fit_transform(number_students))
    [data[n].append(float(scaled_number_students[n])) for n in range(len(data))]

    # define X and y data
    y_data = []
    for row in data:
        y_data.append(row[6])
        row.pop(6)
    X_data = data

    return X_data, y_data, scaler