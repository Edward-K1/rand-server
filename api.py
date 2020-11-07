from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
from decouple import config

from program import run_task, get_full_report, create_server

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
CORS(app)

@app.route('/runtask', methods=['POST'])
def task():
    data = request.get_json(force=True)
    response_data = run_task(data['serverId'],data['time'], data['wallColor'],
                            data['clockColor'], data['labelColor'])
    return make_response(jsonify(response_data), 200)

@app.route('/start', methods=['GET'])
def start():
    response_data = create_server()
    return make_response(jsonify(response_data), 200)

@app.route('/report', methods=['POST'])
def get_report():
    data = request.get_json(force=True)
    response_data = get_full_report(data['serverId'])
    return make_response(jsonify(response_data), 200)

@app.route('/')
def show_clock():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
