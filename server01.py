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
    @app.route('/', methods=['POST'])
    def test():
        return "La conexion Flask conectada"

