from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'Products'}
    return render(request, 'product/index.html', context=context)


def products(request):
    context = {'title': 'Products'}
    return render(request, 'product/products.html', context=context)
