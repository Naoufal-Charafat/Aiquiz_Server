from Juego1 import Juego
# from AiDavinci import Juego
import flask
from util import getApiOpentdb

app = flask.Flask(__name__)


# server.app.run(debug=True)
# print('hola naoufal')
# server.server.send_questions()
# print(server.server.trivia_test())
# Juego.juego("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")
@app.route('/', methods=['GET'])
def capture_request():
    try:
        # typeGame => (1 = juego preguntas respuestas) (2 = juego ai reto)
        typeGame = flask.request.args.get('typeGame')
        if not (typeGame == '1' or typeGame == '2'):
            raise ValueError("El valor typeGame incorrecto")

        # obtener parameters de Game stander
        # ?typeGame=1&category=10&difficulty=easy&type=multiple&language=ES
        if typeGame == '1':
            numberQuestions = 1
            category = flask.request.args.get('category')  # del 9 al 32
            difficulty = flask.request.args.get('difficulty')  # easy;medium;hard
            type_question = flask.request.args.get('type')  # multiple;boolean
            language = flask.request.args.get('language')
            urlApi = getApiOpentdb(numberQuestions, category, difficulty, type_question)
            return Juego.juego(urlApi)

        # obtener parameters de Game AI
        # ?typeGame=2&apiKey=sk-&roundNumber=5&namePlayers=jose;manuel&ProofTruth=P
        if typeGame == '2':
            apiKey = flask.request.args.get('apiKey')
            roundNumber = flask.request.args.get('roundNumber')
            namePlayers = flask.request.args.get('namePlayers')
            # ProofTruth =>> P = prueba / T = verdad
            ProofTruth = flask.request.args.get('ProofTruth')

            return 'Juego AI'

        return 'NULL'

    except Exception as e:
        # Manejo de la excepción
        return f"<h2>Se produjo un error al procesar la solicitud.</h2>" \
               f"<br>Url: {flask.request.url}" \
               f"<br>Error: {e}"


if __name__ == '__main__':
    app.run()
