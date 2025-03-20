from flask import Flask, request, jsonify

from datetime import datetime

app = Flask(__name__)


@app.route('/verificar-data/<ano>-<mes>-<dia>', methods=['GET'])
def verificar_data(ano,mes,dia):
    try:
        ano = int(ano)
        mes = int(mes)
        dia = int(dia)

        data_informada = datetime(ano, mes, dia).date()
        data_atual = datetime.now().date()

        status = ""
        dias_diferenca = data_atual - data_informada
        meses_diferenca = (data_atual.year - data_informada.year) * 12
        anos_diferenca = data_atual.year - data_informada.year


        if data_informada > data_atual:
            status = "futuro"
        elif data_informada < data_atual:
            status = "passado"
        else:
            status = "presente"

            return jsonify({
                'status': status,
                'dias_diferenca': data_informada - data_atual,
                'meses_diferenca': mes - ano,
                'anos_diferenca': ano - ano,
            })
    except ValueError:
        return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)
