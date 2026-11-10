from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    dados = {
        "nome": "Tony Henrique Castro Aguiar",
        "idade": 22,
        "altura": 1.71,
        "profissao": "Estudante de analise e desenvolvimento de sistemas",
        "cursos": ["Administração", "Logica de Programação", "ADS", "Enfermagem"],
        "hobbies": ["Jogar video game", "Assistir filmes de terror", "Ouvir musicas", "Cinema"],
        "cidade": "Portugal, Lisboa",
    }
    return render (request, "inicio.html", dados)

def sobre(request):
    return render(request, "sobre.html")
def contato(request):
    return HttpResponse(
        "<hr>"
                "<a href='/'>Início</a> | "
                "<a href='/sobre/'>Sobre</a> | "
                "<a href='/contato/'>Contato</a>"
"<h1>Entre em contato comigo através do contatos abaixo:</h1>"
        "<p>meuemail@exemplo.com</p>"
        "<p>meu numero de telefone: (99) 99999-9999"
        "<p>meu linkdin: a href= https/aodinqwaiofbwaufab.linkdin.com" )