from django.shortcuts import render

# Create your views here.
def index(request):

    dados = {
        1: {
            'nome': 'Nebulosa de Carina',
            'legenda': 'webbtelescope.org / NASA / James Webb'
        },
        2: {
            'nome': 'Galaxia NGC 1079',
            'legenda': 'nasa.org / NASA / Hubble'
        },
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')

def mais_vistas(request):
    return render(request, 'galeria/mais_vistas.html')

def novas(request):
    return render(request, 'galeria/novas.html')

def surpreenda_me(request):
    return render(request, 'galeria/surpreenda_me.html')