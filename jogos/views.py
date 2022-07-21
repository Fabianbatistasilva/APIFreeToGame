from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    api=requests.get('https://www.freetogame.com/api/games?sort-by=popularity').json()
    cont=0
    for x in api:
        cont+=1
    p = Paginator(api, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        api = p.page(page)
    except (EmptyPage, InvalidPage):
        api = p.page(p.num_pages)
    context={'api':api,'cont':cont}
    return render(request,'home.html',context)
def jogo(request,id):
    jogo=requests.get(f'https://www.freetogame.com/api/game?id={id}').json()
    context={'jogo':jogo,}
    return render(request,'jogo.html',context)


def categoria(request,categoria):
    api=requests.get(f'https://www.freetogame.com/api/games?category={categoria}').json()
    cont=0
    for x in api:
        cont+=1
    p = Paginator(api, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        api = p.page(page)
    except (EmptyPage, InvalidPage):
        api = p.page(p.num_pages)
    context={'api':api,'cont':cont}
    return render(request,'home.html',context)

def plataforma(request,plataforma):
    api=requests.get(f'https://www.freetogame.com/api/games?platform={plataforma}').json()
    cont=0
    for x in api:
        cont+=1
    p = Paginator(api, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        api = p.page(page)
    except (EmptyPage, InvalidPage):
        api = p.page(p.num_pages)
    context={'api':api,'cont':cont}
    return render(request,'home.html',context)


def ordenar(request,ordenacao):
    api=requests.get(f'https://www.freetogame.com/api/games?sort-by={ordenacao}').json()
    cont=0
    for x in api:
        cont+=1
    p = Paginator(api, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        api = p.page(page)
    except (EmptyPage, InvalidPage):
        api = p.page(p.num_pages)
    context={'api':api,'cont':cont}
    return render(request,'home.html',context)