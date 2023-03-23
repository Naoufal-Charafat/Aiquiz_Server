import requests
import openai as ai
import util


class Juego:

    @staticmethod
    def juego(apiOpentdb):
        """
        Funcion obtener las preguntas de la base de datos de opentdb mediante la api
        :return: pregunta +respueta correcta+respuestas incorectas
        """
        # Envía una solicitud GET a la API de OpenTDB
        response = requests.get(apiOpentdb)

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
        respuesta_correcta = data['results'][0]['correct_answer']
        respuestas_incorrectas = data['results'][0]['incorrect_answers']

        text = (f'pregunta: {pregunta} \n'
                f'respuesta_correcta: {respuesta_correcta} \n'
                f'respuestas_incorrectas: {respuestas_incorrectas} \n')

        # traducir más adelante
        # mensaje = util.traducir_texto(text, 'EN', 'ES')
        return data
