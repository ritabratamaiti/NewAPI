import dill
import pandas as pd


def unpack(task):
    ip = open(task + '_model', 'rb')
    model = dill.load(ip)
    ip.close()
    ip = open(task + '_scaler', 'rb')
    scaler = dill.load(ip)
    ip.close()
    return model, scaler


def pre_process(scaler, X):
    scaled_X = scaler.fit_transform(X)
    return (scaled_X)


def predictX(model, scaled_X):
    preds = model.predict(scaled_X)
    temp = []
    for pred in preds:
        if(pred<0):
            pred = 0
        temp.append(pred)
    return (temp)


def make_preds_table(task, dates, preds):
    prediction = pd.DataFrame()
    prediction[task + '_predicted_vals'] = preds
    prediction.index = dates
    return (prediction)


def init_predictor(task, dates, X):
    model, scaler = unpack(task)
    scaled_X = pre_process(scaler, X)
    preds = predictX(model, scaled_X)
    prediction = make_preds_table(task, dates, preds)
    response = prediction.to_json(orient='table')
    return response
