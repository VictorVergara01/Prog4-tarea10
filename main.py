from email import message
from flask import Flask, render_template, request
from api import slangsPa

app = Flask(__name__)

############################################################APPROUTE#######################################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", palabras=slangsPa)

@app.route('/agregar_palabra', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        palabraa = request.form['pa'].capitalize()
        significado = request.form['si']
        nuevo_slang = {
                "palabra": palabraa,
                "significado": significado}
        for palabra in slangsPa:
            if palabra["palabra"] != palabraa:
                existe = palabra
                if len(existe)>0:
                    slangsPa.append(nuevo_slang)
                return render_template('agregar_palabra.html', message=True)
            else:
                return render_template('agregar_palabra.html', message=False)

    return render_template('agregar_palabra.html')    
        
    


@app.route('/editar_palabra', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        Vpalabra = request.form["vpa"].capitalize()
        existe = [palabra for palabra in slangsPa if palabra["palabra"] == Vpalabra]
        if len(existe) > 0:
            Npalabra = request.form["pa"]
            Nsignificado = request.form["si"]
            existe[0]["palabra"] = Npalabra
            existe[0]["significado"] = Nsignificado

            return render_template('editar_palabra.html', Nsignificado=Nsignificado, Npalabra=Npalabra, message=True)
        else:
            return render_template('editar_palabra.html', message=False)

    return render_template('editar_palabra.html')

@app.route('/eliminar_palabra', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        eliminar_palabra = request.form["pa"].capitalize()
        for palabra in slangsPa:
            if palabra["palabra"] == eliminar_palabra:
                existe = palabra
                if len(existe) > 0:
                    slangsPa.remove(existe)
                return render_template('eliminar_palabra.html', message=True)
            else:
                return render_template('eliminar_palabra.html', message=False)

    return render_template('eliminar_palabra.html')


if __name__ == '__main__':
    app.run( debug = True)