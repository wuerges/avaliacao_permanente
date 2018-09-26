from bottle import run, get, post, view, request, redirect
import template as tp

questions = tp.load_questions("simples.mf")

@get('/')
@view('index')
def index():
    return {'questions': questions }


# @post('/send')
# def sendMessage():
#     global nick
#     m = request.forms.get('message')
#     n = request.forms.get('nick')
#     messages.append([n, m])
#     nick = n
#     redirect('/')


run(host='localhost', port=8080)
