# Ingresar todas esas funciones auxiliares que no tengas relacion con la propia clase

from translate import Translator


def traducir_texto(data, idioma_origen, idioma_destino):
    """
    Returns:
        traducir solo preguntas y respuestas del json
    """
    # Crear una instancia de Translator
    translator = Translator(from_lang=idioma_origen, to_lang=idioma_destino)


    # Obtiene la pregunta de los datos recibidos
    pregunta = data['results'][0]['question']
    respuesta_correcta = data['results'][0]['correct_answer']
    respuestas_incorrectas = data['results'][0]['incorrect_answers']

    # Traducir el texto de origen al idioma de destino usando la librería translate
    pregunta_traducido = translator.translate(pregunta)
    respuesta_correcta_traducido = translator.translate(respuesta_correcta)

    respuestas_incorrectas_traducido = [""]
    for respuesta_incorrecta in respuestas_incorrectas:
        aux = translator.translate(respuesta_incorrecta)
        respuestas_incorrectas_traducido.append(aux)

    respuestas_incorrectas_traducido.pop(0)

    #modificar json
    data['results'][0]['question'] = pregunta_traducido
    data['results'][0]['correct_answer'] = respuesta_correcta_traducido
    data['results'][0]['incorrect_answers'] = respuestas_incorrectas_traducido

    return data





def getApiOpentdb(numberQuestions, Category, Difficulty, type_question):
    # Construir la api
    apiOpentdb = f"https://opentdb.com/api.php?" \
                 f"amount={numberQuestions}&" \
                 f"category={Category}&" \
                 f"difficulty={Difficulty}&" \
                 f"type={type_question}"
    return apiOpentdb
