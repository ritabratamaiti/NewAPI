from flask import Flask, jsonify, make_response, request
from api import predictor

app = Flask(__name__)


@app.route("/")
def home():
    return 'Specify a Task!!'


@app.errorhandler(404)
def not_found_error():
    return make_response(jsonify({'error': 'Looks like this task has not yet been defined. :( Sorry.....'}), 404)


@app.route("/predtask", methods=['POST'])
def task_router():
    req = request.get_json(force=True)
    print(req)
    task = req['task']
    try:
        api_call = req['url']
        datautil = __import__(task + '_datautil')
        X, dates = datautil.init_util(api_call)
        response = predictor.init_predictor(task, dates, X)
        return response
    except:
        return not_found_error()

app.run()

# http://api.openweathermap.org/data/2.5/forecast?q=Singapore,SG&appid=4d52e2109f7da2b9fb9579064db1c0f1&mode=json&units=metric
