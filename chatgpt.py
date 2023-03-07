import requests
from bs4 import BeautifulSoup

def enviar_mensaje(message):
    # Hacemos una solicitud GET a la página web
    response = requests.get("https://chat.openai.com/chat")

    # Creamos un objeto BeautifulSoup para analizar el contenido HTML de la página
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    # Encontramos el formulario para enviar mensajes
    form = soup.find("form")

    # Encontramos el campo de entrada de texto para el mensaje
    input_field = form.find("input", {"name": "text"})

    # Establecemos el valor del campo de entrada de texto en nuestro mensaje
    message="Hola, ¿cómo estás?"
    input_field["value"] = message

    # Encontramos el botón de enviar mensaje
    send_button = form.find("button")

    # Enviamos el formulario con el mensaje
    response = requests.post(form["action"], data=form.serialize())

    # Creamos un nuevo objeto BeautifulSoup para analizar la respuesta HTML del servidor
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontramos la respuesta del bot
    bot_response = soup.find("div", {"class": "text-gray-700"}).text.strip()

    # Retornamos la respuesta del bot
    return bot_response

