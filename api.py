from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from program import check_event, reset_values

app = Flask(__name__)
CORS(app)

@app.route('/runtask', methods=['POST'])
def run_task():
    data = request.get_json(force=True)
    response_data = check_event(data['time'], data['wallColor'],
                            data['clockColor'], data['labelColor'])

    return make_response(jsonify(response_data), 200)

@app.route('/start', methods=['GET'])
def start():
    reset_values()
    return make_response(jsonify({"message":"ok"}), 200)




if __name__ == '__main__':
    app.run(debug=True)
