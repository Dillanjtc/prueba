from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # En lugar de devolver solo texto, devolvemos una cadena con estructura HTML
    # Esto permite mostrar imágenes, estilos y formato.
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Saludos Python</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #282c34;
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            h1 {
                margin-bottom: 20px;
                color: #61dafb; /* Un color estilo 'React/Python' */
            }
            img {
                border-radius: 15px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                max-width: 90%;
                height: auto;
            }
            .footer {
                margin-top: 20px;
                font-size: 0.8em;
                color: #aaa;
            }
        </style>
    </head>
    <body>
        <h1>Saludos a todos desde Python 🐍</h1>
        
        <!-- Aquí está el GIF del gato (Gato asintiendo / Vibing Cat) -->
        <img src="https://media1.tenor.com/m/bCcpR0Jp4sIAAAAC/cat-dance.gif" alt="Meme de gato bailando">
        
        <div class="footer">Servidor corriendo en Flask</div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # debug=True permite que el servidor se reinicie si haces cambios en el código
    app.run(host='0.0.0.0', port=5000, debug=True)