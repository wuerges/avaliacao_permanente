from bottle import run, get, post, view, request, redirect
import template as tp
import ofertas as of
import json
import datetime as dt

questions = tp.load_questions("simples.mf")
ofertas = of.load_ofertas("ofertas.mf")

@get('/turma/<codigo>')
@view('index')
def index(codigo):
    return {'questions': questions, 'oferta': ofertas[codigo], 'time': dt.datetime.now() }


@get('/turmas12345')
@view('turmas')
def turmas():
    return {"ofertas": ofertas}

@get('/ok')
@view('ok')
def ok():
    return {}


@post('/send')
def sendForm():

    data = [(k,v) for (k,v) in request.forms.items() ]
    with open("data/responses.json", "a") as f:
        json.dump(data, f)
        f.write("\n")

    redirect('/ok')


run(host='localhost', port=8080)
