import requests
import util


class Juego:

    @staticmethod
    def juego(apiOpentdb, idioma):
        """
        Funcion obtener las preguntas de la base de datos de opentdb mediante la api
        :return: pregunta +respueta correcta+respuestas incorectas
        """
        # Envía una solicitud GET a la API de OpenTDB
        response = requests.get(apiOpentdb)

        # Obtiene los datos de la respuesta en formato JSON
        data = response.json()
        # formato

        if idioma != 'EN':
            data = util.traducir_texto(data, 'EN', idioma)

        return data
