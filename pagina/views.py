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
    return render(request, "contatos.html")

def projetos(request):
    projetos = {
        "projetos": ["Site pessoal", "Sistema de calculadora", "Site SalvaEdu", "Sistema de notas"],
    }
    return render(request, "projetos.html", projetos)