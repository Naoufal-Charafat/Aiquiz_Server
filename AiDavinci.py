import openai
class AiDavinci:
    def __init__(self,api_key):
        openai.api_key = api_key


    @staticmethod
    def message_GPT(message="hola"):
        """
        funcion para obtener resuesta del chatgpt usando la nueva actualziacion de openai API
        :param message: pregutna del usur
        :return: resuesta del chatgpt
        """
        request_ =openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Soy el lider que ordenará juegos, pruebas, retos, preguntas, etc. Mi función es hacer que los integrantes del grupo se lo pasen bien, bebiendo alcohol con responsabilidad y creando situaciones de salseo"},
                {"role": "user", "content": message}
            ]
        )
        cadena = request_['choices'][0]['message']['content']
        return cadena


class Juego:

    @staticmethod
    def juego(ApiUserKey):
        aux = AiDavinci(ApiUserKey)

        jugadores = []  # crea una lista vacía
        n = int(input("¿Cuántos jugadores hay? "))  # pide el número de jugadores
        for i in range(n):  # repite n veces
            nombre = input(f"Introduce el nombre del jugador {i + 1}: ")  # pide el nombre de cada jugador
            jugadores.append(nombre)  # añade el nombre a la lista

        nombres = ", ".join(jugadores)  # une los nombres con comas y espacios



        respuesta = aux.message_GPT("cuentame un chiste que involucre a estos jugadores: " + nombres)

        print(respuesta)

        pass

