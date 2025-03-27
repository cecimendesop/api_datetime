from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)




@app.route('/verificar-data/<data>', methods=['GET'])
def verificar_data(data):
    """
    Verifica a data para definir o período de tempo a qual ela pertence (passado, presente, futuro)

    #Endpoint:
    'GET /verificar-data/<data>'

    :param data: data indicada
    :return: período de tempo a qual ela pertence (passado, presente ou futuro)

    #Resposta (JSON):
    {
            "situacao": status,
            "diferenca": {
                "dias": diferenca_dias,
                "meses": diferenca_meses,
                "anos": diferenca_anos
            }

    #Erros Possíveis:
    {"erro": "Formato de data inválido. Use YYYY-MM-DD."}

    """
    try:
        data_informada = datetime.strptime(data, "%Y-%m-%d").date()
        data_atual = datetime.now().date()
        diferenca_dias = (data_informada - data_atual).days
        diferenca_meses = (data_informada.year - data_atual.year) * 12 + (data_informada.month - data_atual.month)
        diferenca_anos = data_informada.year - data_atual.year

        if data_informada > data_atual:
            status = "futuro"
        elif data_informada < data_atual:
            status = "passado"
        else:
            return jsonify({"situacao": "presente", "diferenca": {"dias": 0, "meses": 0, "anos": 0}})

        return jsonify({
            "situacao": status,
            "diferenca": {
                "dias": diferenca_dias,
                "meses": diferenca_meses,
                "anos": diferenca_anos
            }
        })
    except ValueError:
        return jsonify({"erro": "Formato de data inválido. Use YYYY-MM-DD."}), 400



if __name__ == '__main__':
    app.run(debug=True)


