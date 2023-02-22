
class AiDavinci:
    def __init__(self):
        pass

    def get_response(self):
        """
        Obtenemos una respuesta de la AI
        :return: devolvemos la respuesta = cadena string
        """
        pass

    def check_response(self, response):
        """
        Filtra la respuesta de la AI, es decir que la respuesta tenga un formato especifico
        :return: devolvemos un boleano "True/False"
        """
        pass

    def filter_response(self):
        """
        Esta function se encargará de partir la cadena en 6 partes
        pregunta; opA; opB; opC; opD; respuesta correcta;
        :return: devolvemos 6 VARIABLES A LA VEZ opA; opB; opC; opD; respuesta correcta;
        """
        pass

    def check_count_questions(self):
        """
        En caso de optar por la option B:
        esta function se encarga de verificar que tenemos los X cuestiones listas para su envio
        :return: true/false
        """
        pass



    def get_question(self):
        """
        Esta function se encargará:
            option1: (la proxima pregunta se basa en la respuesta última del usr)
                deberemos de generar la preguntas 1 preguntas = 1 solicitud al servidor, ya que no podemos adivinar
                la respuesta del usr
            option2:(la proxima pregunta se basa en la última respuesta correcta del juego)
                deberemos de generar las x preguntas = 1 solicitud al servidor, es más óptimo y rapido y barato.

        :return: obtener las preguntas
        """
        pass