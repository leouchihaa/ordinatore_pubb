from flask import Flask, request, render_template
import re

app = Flask(__name__)

arraydinomi= []
arrayordinato= []
contatore= 0
flag= False

@app.route('/', methods=['GET', 'POST'])
def start():
    global arraydinomi, contatore, flag
    arraydinomi= []
    arrayordinato= arraydinomi
    contatore= 0
    flag= False
    return render_template('index.html', arraydinomi=arraydinomi, contatore=contatore)
    
@app.route('/inserisci', methods=['GET', 'POST'])
def inserisci():
    global arraydinomi, contatore
    if request.method == 'POST':
        nuovonome= request.form.get('nome')
        arraydinomi.append(str(nuovonome))
        contatore+= 1
    return render_template('index.html', arraydinomi=arraydinomi, contatore=contatore, nuovonome=nuovonome)

@app.route('/ordinamento', methods=['GET', 'POST'])
def ordina():
    global arraydinomi, flag, arrayordinato
    #oppure, per ordinare col bubblesort:
    #arrayordinato= arraydinomi
    #swap= ''
    #for i in range(10):
    #    for j in range(i, 10):
    #            if ( arrayordinato[i] > arrayordinato[j] ):
    #                swap= arrayordinato[i]
    #                arrayordinato[i]= arrayordinato[j]
    #                arrayordinato[j]= swap
    arrayordinato = sorted(arraydinomi, key=str.lower)
    flag= True
    return render_template('index.html', arraydinomi=arraydinomi, arrayordinato=arrayordinato, contatore=contatore, flag=flag)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)
