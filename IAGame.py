import openai
import random
import json
class AiDavinci:


    @staticmethod
    def message_GPT(message):

        request_ =openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Soy el lider que ordenará juegos, pruebas, retos, preguntas, etc. Mi función es hacer que los integrantes del grupo se lo pasen bien, bebiendo alcohol con responsabilidad y creando situaciones de entretenidas para ellos. Mis función serán UNICAMENTE la siguiente generar la pregunta, prueba, o castigo que deberán hacer cada jugador en la última ronda. Debo de ser original y crear retos diferentes en cada ronda. Es muy importante que tenga todo el contexto en cuenta a la hora de desarrollar los retos y preguntas. En la mayoría de estos retos los relacionaré con las rondas anteriores o lo que conozca de los jugadores"},
                {"role": "user", "content": message}
            ]
        )
        cadena = request_['choices'][0]['message']['content']
        return cadena


class Juego:

    @staticmethod
    def juego(datos_json):

        datos = json.loads(datos_json)
        apiKey =  datos["apiKey"]
        contexto = datos["contexto"]
        jugador = datos["jugador"]
        accion = datos["accion"]  # las acciones son p/v/c  prueba verdad o castig

        openai.api_key=apiKey
        print(f'La api key que se ha recibido es:{apiKey} \nEl contexto  que se ha recibido es:{contexto} \nLa accion que se ha recibido es:{accion}')

        contexto=contexto+f"\nRonda 2:\n Turno de {jugador}, esta ronda es de tipo {accion} y es el siguiente: "
        respuesta = AiDavinci.message_GPT(contexto)
        print(f"\n\nTexto generado: {respuesta}")



