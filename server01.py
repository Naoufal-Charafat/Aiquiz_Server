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
    # declaramos que tipo de solicitudes capturamos en este caso reran GETS
    @app.route('/', methods=['GET'])
    def capture_request():
        pregunta = '''<H2>Pregunta: ¿Cuál es el origen de la palabra "fiesta"?</H2><br>
        Opción A: Viene del latín "festum", que significa celebración.<br><br>
        Opción B: Tiene su origen en la lengua griega, con la palabra "heorte", que significa festival.<br><br>
        Opción C: Proviene del idioma árabe, con la palabra "fista", que significa diversión.<br><br>
        Opción D: Deriva del idioma inglés antiguo, con la palabra "feste", que significa festejar.<br><br>'''

        # capturamos los parameters
        user = request.args.get('user')
        cantidad_cuestiones = request.args.get('cantidad_cuestiones')
        tipo = request.args.get('tipo')
        idioma = request.args.get('idioma')

        # crear una function que filtra parameters

        header = f"""
        Jugador: {user}<br><br>
        Cantidad_cuestiones: {cantidad_cuestiones}<br><br>
        Tipo: {tipo}<br><br>
        Idioma: {idioma}<br><br>"""
        respuesta = header + pregunta
        return respuesta

