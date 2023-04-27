from Juego1 import Juego
# from AiDavinci import Juego
import flask
from flask import request
from flask_cors import cross_origin
from util import getApiOpentdb
import json

app = flask.Flask(__name__)


# server.app.run(debug=True)
# print('hola naoufal')
# server.server.send_questions()
# print(server.server.trivia_test())
# Juego.juego("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")
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def capture_request():
    try:
        # typeGame => (1 = juego preguntas respuestas) (2 = juego ai reto)
        typeGame = flask.request.args.get('typeGame')
        if not (typeGame == '1' or typeGame == '2'):
            raise ValueError("El valor typeGame incorrecto")

        # obtener parameters de Game stander
        # local: http://127.0.0.1:5000/?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        # cloud:https://softwebdd.pythonanywhere.com/?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        if typeGame == '1':
            numberQuestions = 1
            category = flask.request.args.get('category')  # del 9 al 32
            difficulty = flask.request.args.get('difficulty')  # easy;medium;hard
            type_question = flask.request.args.get('type')  # multiple;boolean
            language = flask.request.args.get('language')
            urlApi = getApiOpentdb(numberQuestions, category, difficulty, type_question)
            return Juego.juego(urlApi,language)

        # obtener parameters de Game AI
        # local: http://127.0.0.1:5000/?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        # cloud: https://softwebdd.pythonanywhere.com/?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        if typeGame == '2':
            data_entrante = request.get_json()
            print(data_entrante)
            # juego2.juego(data_entrante)


            # Repley test
            datos = {
                "nombre": "Antonio"
            }
            datos_json = json.dumps(datos)
            return datos_json

        return 'NULL'

    except Exception as e:
        # Manejo de la excepción
        return f"<h2>Se produjo un error al procesar la solicitud.</h2>" \
               f"<br>Url: {flask.request.url}" \
               f"<br>Error: {e}"


if __name__ == '__main__':
    app.run()
