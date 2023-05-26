from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Olá, meu nome é Luiz Otávio Jirkowsky e Silva'
