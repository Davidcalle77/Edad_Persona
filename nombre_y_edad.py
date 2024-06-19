
from flask import Flask, request, render_template_string, session
app = Flask(__name__)
# El código `app = Flask(__name__)` crea una instancia de aplicación Flask con el nombre del módulo.
# Esta instancia se usa para definir la aplicación Flask y manejar las peticiones entrantes.
app.secret_key = 'clave_secreta'
@app.route('/', methods=['GET', 'POST'])
# El decorador `@app.route('/', methods=['GET', 'POST'])` de Flask se utiliza para definir una ruta 
# # URL especificada ('/').
# ruta URL especificada ('/').
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_nacimiento = int(request.form['fecha_nacimiento'])
        edad_usuario = 2024 - fecha_nacimiento

        usuarios = session.get('usuarios', [])
        usuarios.append((nombre, edad_usuario)) # Guardar tanto el nombre como la edad del usuario
        session['usuarios'] = usuarios

        return render_template_string('''
            <html>
            <head>
                <title>Información Usuarios</title>
                <style>
                    body {
                        
                        font-family: Arial, sans-serif;
                    }
                    h2 {
                        color: white;
                    }
                    input[type="text"],
                    input[type="number"],
                    input[type="submit"] {
                        padding: 5px;
                        margin-bottom: 5px;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                    }
                    .center {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        background-color:blue; /* Agregar un fondo blanco para el formulario */
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Agregar sombra para mejor visualización */
                    }
                </style>
            </head>
            <body>
                <div class="center">
                    <h2>Informacion Usuario:</h2>
                    {% for usuario, edad in usuarios %}
                        <h3>Nombres: {{ usuario }} </h3>
                        <h3>Edad: {{ edad }} Años</h3>
                    {% endfor %}
                    <button type="button" onclick="window.history.back();">Regresar</button>
                </div>
            </body>
            </html>
        ''', nombre=nombre, edad_usuario=edad_usuario, usuarios=usuarios)

    return '''
        <html>
        <head>
            <title>Informacion Usuarios</title>
            <style>
                body {
                    
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: white;
                }
                input[type="text"],
                input[type="number"],
                input[type="submit"] {
                    padding: 5px;
                    margin-bottom: 5px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                .center {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background-color:blue; /* Agregar un fondo azul para el formulario */
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Agregar sombra para mejor visualización */
                    
                }
            </style>
        </head>
        <body>
            <div class="center">
                <h1>Digite la Información del Usuario</h1>
                <form method="post">
                    Nombres: <input type="text" name="nombre"><br><br>
                    Digite Año Nacimiento: <input type="number" name="fecha_nacimiento"><br><br>
                    <input type="submit" value="Actualizar"><br>
                    <button type="reset">Limpiar</button>
                </form>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

