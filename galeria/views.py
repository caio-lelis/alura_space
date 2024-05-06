from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
# Responsabilidade desses arquivos é de controlar o que será exibido na tela!

def index (request):
    return render(request, 'galeria/index.html')

def imagem (request):
    return render(request, 'galeria/imagem.html')