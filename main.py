import server

# ideas:
#1)
# la solicitud get que obtendremos de la web, un json con las últimas 500 questions para forzar a la ia que
# genere preguntas que no sean las mismas que las últimas 500 questions

from AiDavinci import AiDavinci # importa la clase que has definido en otro archivo

from AiDavinci import Juego #importa la clase que has definido en otro archivo

if __name__ == '__main__':

    server.app.run(debug=True)
    # server.server.send_questions()
    # print(server.server.trivia_test())
    # Juego.juego("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")
