import pandas as pd

def prepare_input(data, scaler):

    #scale percentage columns in data
    data[0] = data[0] / 100
    data[1] = data[1] / 100
    data[2] = data[2] / 100
    data[3] = data[3] / 100
    data[4] = data[4] / 100
    data[5] = data[5] / 100
    data[7] = data[7] / 100

    #scale students amount
    scaled_number = list(scaler.transform(pd.DataFrame([data[8]])))
    data[8] = scaled_number[0]

    return data