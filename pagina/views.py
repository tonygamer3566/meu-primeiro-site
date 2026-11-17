from django.http import HttpResponse
from django.shortcuts import render
from .models import filme
from .models import projeto
from .models import Categoria, projeto
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
        "filme": filme.objects.all(),
        "projeto": projeto.objects.all(),
    }
    return render(request, "projetos.html", projetos)

def categorias(request):
    categorias = {
        "categoria": Categoria.objects.all(),
        "projeto": projeto.objects.all(),
    }
    return render(request, "categorias.html", categorias)

