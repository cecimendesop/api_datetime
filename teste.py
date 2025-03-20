from flask import Flask, request, jsonify

from datetime import datetime, date

app = Flask(__name__)


@app.route('/verificar-data/<data_informada>', methods=['GET'])
def verificar_data(data_informada):
    try:
        datetime.strptime(data_informada, "%Y-%m-%d").now()
        data_informada = request.get_json()

