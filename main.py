# ideas:
#1)
# la solicitud get que obtendremos de la web, un json con las últimas 500 questions para forzar a la ia que
# genere preguntas que no sean las mismas que las últimas 500 questions

from AiDavinci import AiDavinci # importa la clase que has definido en otro archivo

from IAGame import Juego # importa la clase que has definido en otro archivo
import json

if __name__ == '__main__':

    apiKey ="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"
    contexto = "Los jugadores Antonio, María, Alberto y Nina están jugando a prueba o verdad, un juego social para amigos jóvenes que quieren pasarlo bien en un ambiente de fiesta y alcohol. Deberás generar una nueva prueba, verdad o castigo. La prueba será un reto que involucre movimiento, en cambio la verdad será una pregutna. Por otro lado el castigo es una consecuencia que se genera cuando el jugador se niega a hacer una prueba o verdad. Tanto las pruebas, verdades o castigos se adecuarán al contexto y a las rondas que se hayan generado.Las pruebs o verdad serán retos como cantar, hacer imitaciones, atreverse a besar a alguien, recrear situaciones, hacer preguntas íntimas o eróticas, etc. El castigo puede ser desde beber un trago largo de su cubata, quitarse una prenda, hasta estar callado durante un cierto tiempo (1-2 minutos si no beberá). Estas son sus últimas rondas: \nRonda 1:\nTodos los jugadores beben un trago al cubata y están en un ambiente calmado con música de sus gustos a volumen normal, y quieren jugar la siguiente ronda."
    jugador = "Antonio"
    accion = "prueba" #las acciones son p/v/c  prueba verdad o castig

    datos = {
        "apiKey" : apiKey,
        "contexto": contexto,
        "jugador": jugador,
        "accion": accion
    }
    datos_json = json.dumps(datos)      #agrupacion de datos en formato json
    Juego.juego(datos_json)

