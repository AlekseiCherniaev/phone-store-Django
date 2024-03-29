from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'Products'}
    return render(request, 'product/index.html', context=context)


def products(request):
    context = {'title': 'Products',
               'products': [
                   {'id': '1', 'name': 'Product1', 'description': 'About Product1', 'price': '1000', 'image': '...'},
                   {'id': '2', 'name': 'Product2', 'description': 'About Product2', 'price': '1000', 'image': '...'},
                   {'id': '3', 'name': 'Product3', 'description': 'About Product3', 'price': '1000', 'image': '...'}, ]
               }
    return render(request, 'product/products.html', context=context)


def products_for_year(request, year):
    if year > 2025:
        raise Http404()
    context = {'title': f'Products for {year}'}
    return HttpResponse('Products for year ' + str(year))


def product(request, num):
    return HttpResponse(f'Product ' + str(num))


def handler404(request, exception):
    return HttpResponse('Page not found :(')
