from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia



def index(requests):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(exibir=True)
    return render ( requests,'galeria/index.html', {"cards" : fotografias} )

def imagem(requests, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(requests, 'galeria/imagem.html', {'fotografia' : fotografia })

def buscar(requests):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(exibir=True)
    if "buscar" in requests.GET:
        nome_a_buscar = requests.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render (requests, "galeria/buscar.html", {"cards": fotografias})


