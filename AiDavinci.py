import openai
import random

class AiDavinci:
    def __init__(self,api_key):
        openai.api_key = api_key

    @staticmethod
    def message_GPT(message="No hay mensaje"):
        """
        funcion para obtener resuesta del chatgpt usando la nueva actualziacion de openai API
        :param message: pregutna del usur
        :return: resuesta del chatgpt
        """
        request_ =openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Soy el lider que ordenará juegos, pruebas, retos, preguntas, etc. Mi función es hacer que los integrantes del grupo se lo pasen bien, bebiendo alcohol con responsabilidad y creando situaciones de salseo. mis respuestas serán UNICAMENTE la pregunta, prueba, o castigo que deberán hacer cada jugador. Debo de ser original y crear retos diferentes en cada ronda. Es muy importante que tenga todo el contexto en cuenta a la hora de desarrollar los retos y preguntas. En la mayoría de estos retos los relacionaré con las rondas anteriores"},
                {"role": "user", "content": message}
            ]
        )
        cadena = request_['choices'][0]['message']['content']
        return cadena


class Juego:

    @staticmethod
    def juego(ApiUserKey,jugadores0=None):
        aux = AiDavinci(ApiUserKey)

        jugadores = []  # crea una lista vacía
        # pide el número de jugadores
        n=3
        for i in range(n):  # repite n veces
            nombre = input(f"Introduce el nombre del jugador {i+1}:")  # pide el nombre de cada jugador
            jugadores.append(nombre)  # añade el nombre a la lista
            nombres = ", ".join(jugadores)  # une los nombres con comas y espacios


        contexto = f"El contexto es el siguiente, los jugadores {nombres} están jugando a prueba o verdad, un juego social para amigos jóvenes que quieren pasarlo bien en un ambiente de fiesta y alcohol. Los retos son retos como darle un beso a alguien, hacer alguna imitación, hacer alguna posicion extraña, cantar algo. El castigo puede ser desde beber un trago largo de su cubata, quitarse una prenda, hasta estar callado durante un cierto tiempo (1-2 minutos si no beberá). Estas son sus últimas rondas: \nRonda 1:\nTodos los jugadores beben un trago al cubata y están en un ambiente calmado con música de sus gustos a volumen normal, y quieren jugar la siguiente ronda."
        rondas = 12  # establece el número de rondas del juego




        for r in range(rondas):  # repite rondas veces

            print(f"Ronda {r + 1} de {rondas}")  # muestra el número de la ronda actual
            elegido = random.choice(jugadores)  # elige un jugador al azar de la lista
            print(f"!Es el turno de {elegido}!")  # muestra el nombre del jugador elegido


            opcion = input("¿Prueba (p) o verdad(v)? ")  # pide al jugador que elija entre verdad o reto


            if opcion.lower() == "v":  # si elige verdad
                pregunta = aux.message_GPT(f"Haz una pregunta personal al jugador{elegido}, puede ser una pregunta de cualquier tipo, desde cual ha sido su mejor polvo hasta su primer beso. Debe de ser una pregunta que se tenga que responder de manera oral. te en cuena el contexto que te escribo al final." + elegido + ".\n\n" + contexto)
                print(pregunta)  # genera y muestra una pregunta personal usando la API y el contexto

                # pide al jugador que diga si ha hecho o no el reto
                resultado = input(f"{elegido}. ¿Quieres responder? (s/n): ")

                if resultado.lower() == "s":  # si decide responder
                    respuesta = input("Respuesta: ")  # pide al jugador que responda a la pregunta
                    contexto += f"\nRonda {r + 2}:\n{elegido} eligió verdad y respondió lo siguiente: " + respuesta  # actualiza el contexto con el resultado del jugador


                elif resultado.lower() == "n":  # si decide no responder
                    castigo = aux.message_GPT("Dale un castigo al jugador " + elegido + " por no hacer su reto. ten en cuenta el contexto global.\n\n" + contexto)
                    print(castigo)  # genera y muestra un castigo usando la API y el contexto
                    contexto += f"{elegido} eligió verdad pero no lo hizo, así que recibió el siguiente castigo: {castigo}\n\n"  # actualiza el contexto con el castigo del jugador





            elif opcion.lower() == "p":  # si elige consecuencia
                reto = aux.message_GPT("Dale un reto divertido al jugador " + elegido + ", teneindo en cuenta el contexto que te escribo al final. .\n\n" + contexto)
                print(reto)  # genera y muestra un reto divertido usando la API y el contexto

                # pide al jugador que diga si ha hecho o no el reto
                resultado = input(f"{elegido,}¿Has hecho el reto? (s/n): ")

                if resultado.lower() == "s":  # si ha hecho el reto
                 contexto += f"\nRonda {r+2}:\n{elegido} eligió reto y cumplió con su siguiente reto: "+ reto  # actualiza el contexto con el resultado del jugador


                elif resultado.lower() == "n":  # si no ha hecho el reto
                    castigo = aux.message_GPT("Dale un castigo al jugador " + elegido + " por no hacer su reto. ten en cuenta el contexto global.\n\n" + contexto)
                    print(castigo)  # genera y muestra un castigo usando la API y el contexto
                    contexto += f"{elegido} eligió reto pero no lo hizo, así que recibió el siguiente castigo: {castigo}\n\n"  # actualiza el contexto con el castigo del jugador

    print("El juego ha terminado. Gracias por jugar.")
pass

