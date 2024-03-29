from django.http import HttpResponse, Http404
from django.shortcuts import render
from product import models


# Create your views here.
def index(request):
    context = {'title': 'Main Page'}
    return render(request, 'product/index.html', context=context)


def products(request):
    context = {'title': 'Products',
               'products': models.PhoneProduct.objects.all(),
               'categories': models.PhoneCategory.objects.all(),
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
