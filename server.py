import flask
import requests
import openai as ai
import util

app = flask.Flask(__name__)


class server:

    def __init__(self):
        pass

    def send_questions(self):
        """
        esta funcion obtiene las questiones y los envia a la web
        :return:
        """
        pass

    @staticmethod
    # declaramos que tipo de solicitudes capturamos en este caso seran GETS
    @app.route('/', methods=['GET'])
    def capture_request():
        pregunta = '''<H2>Pregunta: ¿Cuál es el origen de la palabra "fiesta"?</H2><br>
        Opción A: Viene del latín "festum", que significa celebración.<br><br>
        Opción B: Tiene su origen en la lengua griega, con la palabra "heorte", que significa festival.<br><br>
        Opción C: Proviene del idioma árabe, con la palabra "fista", que significa diversión.<br><br>
        Opción D: Deriva del idioma inglés antiguo, con la palabra "feste", que significa festejar.<br><br>'''

        # capturamos los parameters
        user = flask.request.args.get('user')
        cantidad_cuestiones = flask.request.args.get('cantidad_cuestiones')
        tipo = flask.request.args.get('tipo')
        idioma = flask.request.args.get('idioma')

        # crear una function que filtra parameters

        # Al enviar la respuesta a la solicitude get, como la respuesta será imprimida en el navegador el code HTML
        # se interpretara correctamente lo cual nos da muchas posibilidades de como queramos ejecutar la pagina del juego
        # podemos enviar páginas completas como solicitude get asi enviamos un code o otro en function del tipo del juego
        # ventajas:
        # con una sola página podemos ejecutar un juego o otro, eso si los archivos css y js deben de estar almacenados en el
        # servidor en caso de que se ejecute un post o otro

        header = f"""
        Jugador: {user}<br><br>
        Cantidad_cuestiones: {cantidad_cuestiones}<br><br>
        Tipo: {tipo}<br><br>
        Idioma: {idioma}<br><br>"""
        respuesta = header + pregunta

        return "null"

    @staticmethod
    def trivia_test():
        """
        Funcion obtener las preguntas de la base de datos de opentdb mediante la api
        :return: pregunta +respueta correcta+respuestas incorectas
        """
        # Envía una solicitud GET a la API de OpenTDB
        cantidad_preguntas = 1
        difficulty = "easy"
        type = 'multiple'
        response = requests.get(
            f"https://opentdb.com/api.php?amount={cantidad_preguntas}&category=21&difficulty={difficulty}&type={type}")

        # Obtiene los datos de la respuesta en formato JSON
        data = response.json()
        # formato
        """
                {
           "response_code":0,
           "results":[
              {
                 "category":"Sports",
                 "type":"multiple",
                 "difficulty":"easy",
                 "question":"How many soccer players should be on the field at the same time?",
                 "correct_answer":"22",
                 "incorrect_answers":[
                    "20",
                    "24",
                    "26"
                 ]
              },
              {
                 "category":"Sports",
                 "type":"multiple",
                 "difficulty":"easy",
                 "question":"When was the FC Schalke 04 founded?",
                 "correct_answer":"1904",
                 "incorrect_answers":[
                    "1909",
                    "2008",
                    "1999"
                 ]
              }
           ]
        }
        """
        # Obtiene la pregunta de los datos recibidos
        pregunta = data['results'][0]['question']
        respuesta_correcta= data['results'][0]['correct_answer']
        respuestas_incorrectas = data['results'][0]['incorrect_answers']

        text = (f'pregunta: {pregunta} \n'
              f'respuesta_correcta: {respuesta_correcta} \n'
              f'respuestas_incorrectas: {respuestas_incorrectas} \n')

        mensaje = util.traducir_texto(text,'EN','ES')
        return mensaje

    # ------------------------------------------testing-----------------------------------------------
    # en esta function comprobamos si caput ramos bien la solicitud get y devolver una respuesta a dicha solicitude
    @staticmethod
    def test_flask():
        app.run(debug=True)

