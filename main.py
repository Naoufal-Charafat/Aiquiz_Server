from Juego1 import Juego as juego1
from IAGame import Juego as juego2
import flask
from flask import request
from flask_cors import cross_origin
from util import getApiOpentdb

import mysql.connector

app = flask.Flask(__name__)
def chatbotEPS(datos_json):
    # obtener datos
    sentencia = datos_json['consultas']

    # Crea una conexión a la base de datos
    mydb = mysql.connector.connect(
        host="sql205.your-server.de",
        user="wp_yosta_6 ",
        password="mkNMTMWQ4Zcg85GX",
        database="wp_yosta_db6"
    )

    # Comprueba si la conexión fue exitosa
    if mydb.is_connected():
        # Ejecuta la consulta SQL
        mycursor = mydb.cursor()
        mycursor.execute(sentencia)

        # Obtén los resultados de la consulta
        rows = mycursor.fetchall()
    # Cierra la conexión a la base de datos
    mydb.close()

    return rows



@app.route('/', methods=['POST'])
@cross_origin()
def capture_request():
    try:
        # typeGame => (1 = juego preguntas respuestas) (2 = juego ai reto)
        typeGame = flask.request.args.get('typeGame')
        if not (typeGame == 'quiz' or typeGame == 'aiquiz' or typeGame == 'chatbot'):
            raise ValueError("El valor typeGame incorrecto")

        # obtener parameters de Game stander
        # local: http://127.0.0.1:80/?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        # cloud:https://softwebdd.pythonanywhere.com/?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        # local&cloud:https://9004-154-60-243-237.ngrok-free.app/?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        if typeGame == 'quiz':
            numberQuestions = 1
            category = flask.request.args.get('category')  # del 9 al 32
            difficulty = flask.request.args.get('difficulty')  # easy;medium;hard
            type_question = flask.request.args.get('type')  # multiple;boolean
            language = flask.request.args.get('language')
            urlApi = getApiOpentdb(numberQuestions, category, difficulty, type_question)

            # la funcion juego1 devuelve json
            return juego1.juego(urlApi, language)

        # obtener parameters de Game AI
        # local: http://127.0.0.1:80/?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        # cloud: https://softwebdd.pythonanywhere.com/?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        # local&cloud:https://9004-154-60-243-237.ngrok-free.app/?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        if typeGame == 'aiquiz':
            _request1 = request.get_json()
            print("=======Request=======")
            print(_request1)

            print("======Repley======")
            # la funcion juego2 debe devolver json
            _repley1 = juego2.juego(_request1)
            print(_repley1)

            """# Repley test
            datos = {
                "nombre": "Antonio"
            }
            datos_json = json.dumps(datos)"""
            return _repley1

        # obtener datos de la BD-Mysql y enviar datos al chatbot
        # local: http://127.0.0.1:80/?typeGame=chatbot
        # cloud:https://softwebdd.pythonanywhere.com/?typeGame=chatbot
        # local&cloud:https://9004-154-60-243-237.ngrok-free.app/?typeGame=chatbot
        if typeGame == 'chatbot':
            _request2 = request.get_json()
            return chatbotEPS(_request2)

    except Exception as e:
        # Manejo de la excepción
        return f"<h2>AiQUIZ Se produjo un error al procesar la solicitud.</h2>" \
               f"<br>Url: {flask.request.url}" \
               f"<br><br>Error: {e}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=False)
