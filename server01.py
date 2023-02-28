from flask import Flask, request
app = Flask(__name__)
class server:

    def __init__(self):
        pass

     # utilizar la lebreria Flask

    def send_questions(self):
        """
        esta funcion obtiene las questiones y los envia a la web
        :return:
        """
        pass


    def main(self):
        """
        Esta function raiz se encargará de llevar a cabo la ejecución de server para que esté en escucha
        en tiempo real para posibles solicitudes de la web http
        :return: la respuesta se envia formato JSON
        """
        pass


    @staticmethod
    @app.route('/', methods=['GET'])
    def capture_request():
        pregunta = '''<H2>Pregunta: ¿Cuál es el origen de la palabra "fiesta"?</H2><br>
        Opción A: Viene del latín "festum", que significa celebración.<br><br>
        Opción B: Tiene su origen en la lengua griega, con la palabra "heorte", que significa festival.<br><br>
        Opción C: Proviene del idioma árabe, con la palabra "fista", que significa diversión.<br><br>
        Opción D: Deriva del idioma inglés antiguo, con la palabra "feste", que significa festejar.<br><br>'''

        # capturamos los parametros
        gamer = request.args.get('user')

        header = f"Jugador: {gamer}<br><br>"
        respuesta = header + pregunta
        return respuesta

