from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import filme
from .models import projeto
from .models import Categoria, projeto
from .forms import projetoForm


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

def novo_projeto(request):
    if request.method == "POST":
        form = projetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = projetoForm()
    return render(request, "novo_projeto.html", {"form": form, "projeto": None})

def detalhe_projeto(request, id):
    projeto = get_object_or_404(projeto, id=id)
    return render(request, "detalhe_projeto.html", {"projeto": projeto})


def editar_projeto(request, id):
    projeto_obj = get_object_or_404(projeto, id=id)

    if request.method == "POST":
        form = projetoForm(request.POST, instance=projeto_obj)
        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = projetoForm(instance=projeto_obj)

    return render(request, "novo_projeto.html", {"form": form, "projeto": projeto_obj})


def excluir_projeto(request, id):
    projeto_obj = get_object_or_404(projeto, id=id)

    if request.method == "POST":
        projeto_obj.delete()
        return redirect("projetos")

    return render(request, "excluir_projeto.html", {"projeto": projeto_obj})