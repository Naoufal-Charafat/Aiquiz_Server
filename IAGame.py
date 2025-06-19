import openai
import json
import base64
from elevenlabs import generate


class elevenlabs:
    @staticmethod
    def generateAudio(message):
        # eleven_api_key =  
        eleven_api_key = 
        audio = generate(
            text=message,
            api_key= eleven_api_key,
            voice="Bella",
            model='eleven_multilingual_v1'
        )
        # save(audio, "audio/outputAI.wav")
        return audio

class GPT:
    @staticmethod
    def message_GPT(message):
        request_ = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Soy el lider que ordenará juegos, pruebas, retos, preguntas, etc. Mi función es hacer que los integrantes del grupo se lo pasen bien, bebiendo alcohol con responsabilidad y creando situaciones de entretenidas para ellos. Mis función serán UNICAMENTE la siguiente generar la pregunta, prueba, o castigo que deberán hacer cada jugador en la última ronda. Debo de ser original y crear retos diferentes en cada ronda. Es muy importante que tenga todo el contexto en cuenta a la hora de desarrollar los retos y preguntas. En la mayoría de estos retos los relacionaré con las rondas anteriores o lo que conozca de los jugadores"},
                {"role": "user", "content": message}
            ]
        )
        cadena = request_['choices'][0]['message']['content']
        return cadena

class Juego:
    @staticmethod
    def juego(datos_json):
        # get data json web
        apiKey = datos_json["apiKey"]
        contexto = datos_json["contexto"]
        Generar_audio_bool = datos_json["audio"]

        openai.api_key = apiKey
        request = GPT.message_GPT(contexto)

        if(Generar_audio_bool == True):
            audio = elevenlabs.generateAudio(request)
            audio_base64 = base64.b64encode(audio).decode('utf-8')  # Convertir el audio a base64
            request_json = {
                "contexto": request,
                "audio": audio_base64
            }
        else:
            request_json = {
                "contexto": request
            }

        return json.dumps(request_json)
