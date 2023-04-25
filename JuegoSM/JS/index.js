const questions = [
    {
        
        //escribir lo mismo pero en español
        question: "¿Cuántos días hacen una semana?",
        optionA: "10 días",
        optionB: "14 días",
        optionC: "5 días",
        optionD: "7 días",
        correctOption: "optionD"
    },

    {
        
        //escribir lo mismo pero en español
        question: "¿Cuántos jugadores están permitidos en un campo de fútbol?",
        optionA: "10 jugadores",
        optionB: "11 jugadores",
        optionC: "9 jugadores",
        optionD: "12 jugadores",
        correctOption: "optionB"
    },

    {
        
        //escribir lo mismo pero en español
        question: "¿Quién fue el primer presidente de los Estados Unidos?",
        optionA: "Donald Trump",
        optionB: "Barack Obama",
        optionC: "Abraham Lincoln",
        optionD: "George Washington",
        correctOption: "optionD"

    },

    {
        //escribir lo mismo pero en español
        question: "30 días tiene..... ?",
        optionA: "Enero",
        optionB: "Diciembre",
        optionC: "Junio",
        optionD: "Agosto",
        correctOption: "optionC"
    },

    {
        
        //escribir lo mismo pero en español
        question: "¿Cuántas horas hay en un día?",
        optionA: "30 horas",
        optionB: "38 horas",
        optionC: "48 horas",
        optionD: "24 horas",
        correctOption: "optionD"
    },

    {
       
        //escribir lo mismo pero en español
        question: "¿Cuál es el río más largo del mundo?",
        optionA: "Río Nilo",
        optionB: "Río Largo",
        optionC: "Río Níger",
        optionD: "Lago Chad",
        correctOption: "optionA"
    },


]


let shuffledQuestions = [] //array vacío para contener preguntas seleccionadas aleatoriamente

function handleQuestions() { 
    //función para barajar y agregar 10 preguntas al array shuffledQuestions
    while (shuffledQuestions.length <= 5) {
        const random = questions[Math.floor(Math.random() * questions.length)]
        if (!shuffledQuestions.includes(random)) {
            shuffledQuestions.push(random)
        }
    }
}


let questionNumber = 1 //variable para mostrar el número de pregunta en el DOM
//let playerScore = 0  
let wrongAttempt = 0 //variable para contar el número de respuestas incorrectas
let indexNumber = 0 //variable para acceder a la pregunta actual en el array de preguntas

//función para mostrar la siguiente pregunta en la interfaz
function NextQuestion(index) {
    handleQuestions() //llama a la función para barajar las preguntas
    const currentQuestion = shuffledQuestions[index]
    document.getElementById("question-number").innerHTML = questionNumber //muestra el número de pregunta en el DOM
    //document.getElementById("player-score").innerHTML = playerScore
    document.getElementById("display-question").innerHTML = currentQuestion.question; //muestra la pregunta en el DOM
    document.getElementById("option-one-label").innerHTML = currentQuestion.optionA; //muestra las opciones en el DOM
    document.getElementById("option-two-label").innerHTML = currentQuestion.optionB; //muestra las opciones en el DOM
    document.getElementById("option-three-label").innerHTML = currentQuestion.optionC; //muestra las opciones en el DOM
    document.getElementById("option-four-label").innerHTML = currentQuestion.optionD; //muestra las opciones en el DOM

}

//función para comprobar la respuesta
function checkForAnswer() {
    //
    const currentQuestion = shuffledQuestions [indexNumber] //obtiene la pregunta actual
    const currentQuestionAnswer = currentQuestion.correctOption //obtiene la respuesta correcta de la pregunta actual
    const options = document.getElementsByName("option"); //obtiene todos los inputs de tipo radio
    let correctOption = null //variable para guardar el id del input correcto
    //recorre los inputs de tipo radio para obtener el id del input correcto
    options.forEach((option) => {
        //compara el valor del input con la respuesta correcta de la pregunta actual
        if (option.value === currentQuestionAnswer) {
            
            correctOption = option.labels[0].id //guarda el id del input correcto
        }
    })
   
    //comprueba si el usuario ha seleccionado una opción
    if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
        document.getElementById('option-modal').style.display = "flex"
    }

    //recorre los inputs de tipo radio para comprobar si la respuesta es correcta o incorrecta
    options.forEach((option) => {
        if (option.checked === true && option.value === currentQuestionAnswer) {
            document.getElementById(correctOption).style.backgroundColor = "green"
            playerScore++
            indexNumber++
            //
            setTimeout(() => {
                questionNumber++
            }, 1000)
        }
        //comprueba si la respuesta es incorrecta
        else if (option.checked && option.value !== currentQuestionAnswer) {
            const wrongLabelId = option.labels[0].id
            document.getElementById(wrongLabelId).style.backgroundColor = "red"
            document.getElementById(correctOption).style.backgroundColor = "green"
            wrongAttempt++
            indexNumber++
            
            setTimeout(() => { 
                questionNumber++
            }, 1000)
        }
    })
}



//función para manejar el final del juego
function handleNextQuestion() {
    checkForAnswer()
    unCheckRadioButtons()
    //
    setTimeout(() => {
        if (indexNumber <= 9) {
            NextQuestion(indexNumber)
        }
        else {
            handleEndGame()
        }
        resetOptionBackground()
    }, 1000);
}

//
function resetOptionBackground() {
    const options = document.getElementsByName("option");
    options.forEach((option) => {
        document.getElementById(option.labels[0].id).style.backgroundColor = ""
    })
}

//función para deseleccionar los inputs de tipo radio
function unCheckRadioButtons() {
    const options = document.getElementsByName("option");
    for (let i = 0; i < options.length; i++) {
        options[i].checked = false;
    }
}

//función para manejar el final del juego
function handleEndGame() {
    let remark = null
    let remarkColor = null

   //comprueba  puntuacion del jugador
    if (playerScore <= 3) {
        remark = "Bad Grades, Keep Practicing."
        remarkColor = "red"
    }
    else if (playerScore >= 4 && playerScore < 7) {
        remark = "Average Grades, You can do better."
        remarkColor = "orange"
    }
    else if (playerScore >= 7) {
        remark = "Excellent, Keep the good work going."
        remarkColor = "green"
    }
    const playerGrade = (playerScore / 10) * 100

   //muestra los resultados
    document.getElementById('remarks').innerHTML = remark
    document.getElementById('remarks').style.color = remarkColor
    document.getElementById('grade-percentage').innerHTML = playerGrade
    document.getElementById('wrong-answers').innerHTML = wrongAttempt
    document.getElementById('right-answers').innerHTML = playerScore
    document.getElementById('score-modal').style.display = "flex"

}

//funcion para cerrar el modal de resultados
function closeScoreModal() {
    questionNumber = 1
    playerScore = 0
    wrongAttempt = 0
    indexNumber = 0
    shuffledQuestions = []
    NextQuestion(indexNumber)
    document.getElementById('score-modal').style.display = "none"
}

//funcion para cerrar el modal de opciones
function closeOptionModal() {
    document.getElementById('option-modal').style.display = "none"
}