from django.shortcuts import render


def index(requests):
    return render(requests,'galeria/index.html')

def imagem(requests):
    return render(requests, 'galeria/imagem.html')

