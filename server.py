from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="Vida es complicada"

@app.route('/')
def hola_mundo():
    if "contador" not in session:
        session['contador'] = 1
    else:
        session['contador'] += 1

    return render_template('index.html')

@app.route('/destroy_session')
def destruir():
    session.clear()
    return redirect('/')

@app.route('/aumento')
def adios_mundo():
    session['contador']+=1
    return redirect('/')

@app.route('/reseteo')
def resset():
    session.clear()
    return redirect('/')

@app.route('/conta', methods=['POST'])
def numeral():
    session['contador']+= int(request.form['cuenta'])-1
    return redirect ('/')




if __name__ == "__main__":
    app.run(debug=True)