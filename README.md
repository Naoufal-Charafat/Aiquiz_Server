# 🎮 AI Quiz Game - Juegos Sociales con IA

## 📝 Descripción

AI Quiz Game es una innovadora plataforma de juegos sociales que combina la diversión de los juegos de preguntas tradicionales con la potencia de la inteligencia artificial. Diseñada para grupos de amigos que buscan entretenimiento interactivo, la aplicación ofrece múltiples modalidades de juego incluyendo trivia clásica y el popular "Verdad o Reto" potenciado con IA.

## ✨ Características principales

- 🤖 **Integración con GPT-3.5**: Genera preguntas, retos y castigos personalizados usando IA
- 🎯 **Múltiples modos de juego**:
  - Quiz tradicional con preguntas de cultura general
  - Verdad o Reto con IA que adapta los desafíos según el contexto
- 🌐 **API REST**: Backend robusto para servir preguntas y gestionar partidas
- 🎨 **Interfaz responsiva**: Diseño adaptable para dispositivos móviles y desktop
- 🔊 **Generación de audio**: Convierte texto a voz usando ElevenLabs
- 🌍 **Multiidioma**: Soporte para traducción automática de preguntas
- 👥 **Multijugador**: Soporte para 2-25 jugadores simultáneos

## 📸 Capturas de pantalla

*[Las capturas de pantalla deberían añadirse aquí mostrando las diferentes pantallas del juego]*

- Pantalla de selección de jugadores
- Interfaz de preguntas del quiz
- Pantalla de Verdad o Reto
- Resultados y puntuaciones

## 🛠️ Tecnologías utilizadas

### Backend
- 🐍 **Python 3.x**
- 🌶️ **Flask** - Framework web
- 🔌 **Flask-CORS** - Manejo de CORS
- 🤖 **OpenAI API** - Integración con GPT-3.5
- 🗄️ **MySQL** - Base de datos
- 🔊 **ElevenLabs API** - Síntesis de voz
- 🌐 **Beautiful Soup** - Web scraping

### Frontend
- 🌐 **HTML5**
- 🎨 **CSS3** - Diseño responsivo
- ⚡ **JavaScript** - Lógica del cliente
- 🎭 **Google Fonts** - Tipografías personalizadas

### APIs Externas
- 📚 **Open Trivia Database** - Preguntas de cultura general
- 🤖 **OpenAI GPT-3.5** - Generación de contenido
- 🔊 **ElevenLabs** - Text-to-Speech

## 🚀 Instalación y uso

### Requisitos previos
```bash
- Python 3.8+
- pip
- MySQL
- Clave API de OpenAI
- Clave API de ElevenLabs (opcional)
```

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/ai-quiz-game.git
cd ai-quiz-game
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno**
```python
# En config.py añadir:
OPENAI_API_KEY = "tu-clave-api"
ELEVENLABS_API_KEY = "tu-clave-api"
```

4. **Configurar base de datos**
```sql
# Configurar conexión MySQL en main.py
host="tu-servidor"
user="tu-usuario"
password="tu-contraseña"
database="chatbotEPS"
```

5. **Ejecutar el servidor**
```bash
python main.py
```

### Uso

#### API Endpoints

**Quiz tradicional:**
```
GET /?typeGame=quiz&category=10&difficulty=easy&type=multiple&language=ES
```

**Verdad o Reto con IA:**
```
POST /?typeGame=aiquiz
Body: {
    "apiKey": "sk-...",
    "contexto": "contexto del juego",
    "audio": true/false
}
```

## 📁 Estructura del proyecto

```
ai-quiz-game/
│
├── 📄 main.py              # Servidor Flask principal
├── 📄 config.py            # Configuración y claves API
├── 📄 util.py              # Funciones auxiliares
│
├── 🎮 Juegos/
│   ├── AiDavinci.py        # Lógica del juego con IA
│   ├── IAGame.py           # Gestor de juegos con IA
│   └── Juego1.py           # Quiz tradicional
│
└── 🌐 JuegoSM/
    ├── 📁 CSS/             # Estilos de la interfaz
    ├── 📁 JS/              # Lógica del frontend
    └── 📄 *.html           # Páginas del juego
```

## 👥 Autores / Colaboradores

- 👨‍💻 **Desarrollador Principal** - *Creación del backend y lógica de juegos*
- 🎨 **Diseñador UI/UX** - *Interfaz y experiencia de usuario*

*¿Quieres contribuir? ¡Las pull requests son bienvenidas!*

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 💼 Contacto para empresas / Colaboraciones

¿Interesado en usar AI Quiz Game en tu empresa o evento? ¿Quieres colaborar en el desarrollo?

📧 **Email**: contacto@aiquizgame.com  
💬 **Discord**: AIQuizGame#1234  
🐦 **Twitter**: @AIQuizGame  

### 🤝 Oportunidades de colaboración:
- Integración en eventos corporativos
- Personalización para marcas
- Desarrollo de nuevas modalidades
- Traducciones y localización

---

⭐ **¡No olvides dar una estrella al proyecto si te gustó!** ⭐

🎯 *Hecho con ❤️ y mucha ☕ por el equipo de AI Quiz Game*
