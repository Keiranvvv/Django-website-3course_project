from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Главная страница - Главная',
        'content': "",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Главная страница - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }
    return render(request, 'main/about.html', context)

def delivery(request):
    context = {
        'title': 'Доставка и оплата - Доставка',
        'content': "Доставка",
        'text_on_page': "Здесь вы можете ознакомиться с условиями доставки."
    }

    return render(request, 'main/delivery.html', context)