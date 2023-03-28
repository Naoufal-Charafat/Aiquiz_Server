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

def seleccionSala(categoria, idioma,dif,tipo):
    datoscategorias = ['Any Category','General Knowledge','Books','Film','Music','Musicals & Theatres','Television','Videogames','Board Games','Science & Nature','Computers','Mathematics','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Comics','Gadgets','Japanese Anime & Manga','Cartoon & Animations']
    datosIdioma = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'in', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur']
    dificultad = ['Any Difficulty','Easy','Medium','Hard']
    type = ['Any Type','Multiple Choice','True/False']
    for cat_aux in datoscategorias:
        for idi_aux in datosIdioma:
            for dif_aux in dificultad:
                for typ_aux in type:
                    if categoria == cat_aux and idioma == idi_aux and dif == dif_aux and tipo == typ_aux:
                     return True

    return False


resultado = seleccionSala('Art','ar','Hard','True/False')
print(resultado)




