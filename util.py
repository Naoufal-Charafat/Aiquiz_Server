# Ingresar todas esas funciones auxiliares que no tengas relacion con la propia clase

from translate import Translator

def traducir_texto(texto: str, idioma_origen: str, idioma_destino: str) -> str:
    """Traduce un texto desde el idioma de origen al idioma de destino usando la librería translate.

    Args:
        texto: El texto a traducir.
        idioma_origen: El idioma del texto de origen (por ejemplo, 'es' para español).
        idioma_destino: El idioma de destino para la traducción (por ejemplo, 'en' para inglés).

    Returns:
        El texto traducido en el idioma de destino.
    """
    # Crear una instancia de Translator
    translator = Translator(from_lang=idioma_origen, to_lang=idioma_destino)

    # Traducir el texto de origen al idioma de destino usando la librería translate
    texto_traducido = translator.translate(texto)

    return texto_traducido

# Ejemplo idiomas

