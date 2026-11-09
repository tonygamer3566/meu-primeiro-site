from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    dados = {
        "nome": "Tony Henrique Castro Aguiar",
        "idade": 22,
        "altura": 1.71,
        "profissao": "estudante de analise e desenvolvimento de sistemas",
        "pets": ["gato", "cachorro", "hamster", "peixe"],
    }
    return render (request, "inicio.html", dados)

def sobre(request):
    return HttpResponse("<p>Este é um site criado sobre mim.</p>")

def contato(request):
    return HttpResponse(
"<h1>Entre em contato comigo através do e-mail:</h1>"
        "<p>meuemail@exemplo.com</p>"
        "<hr>"
        "<a href='/'>Início</a> | "
        "<a href='/sobre/'>Sobre</a> | "
        "<a href='/contato/'>Contato</a>" )