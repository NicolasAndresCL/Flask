from flask import Flask, render_template, render_template_string, request, url_for # Importa render_template

app = Flask(__name__)



@app.route('/post_ejemplo', methods=['POST']) # usar con Postman 
def post_ejemplo():
    return render_template_string('''
        <h1>Ejemplo de POST</h1>
        <p>Esta es una página de ejemplo para mostrar cómo manejar un POST.</p>
        <<p><a href="{{ url_for('home') }}">Volver al inicio</a></p>
''')
       
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/get_ejemplo')
def get_ejemplo():
    return render_template("get_ejemplo.html")


if __name__ == '__main__':
    app.run(debug=True)