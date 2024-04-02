from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from product import models
from product.models import PhoneProduct
from product import forms


# Create your views here.
def index(request):
    context = {'title': 'Main Page'}
    return render(request, 'product/index.html', context=context)


def products(request):
    context = {'title': 'Products',
               'products': models.PhoneProduct.phone_objects.all(),
               'categories': models.PhoneCategory.objects.all(),
               'tags': models.PhoneTag.objects.all(),
               }
    return render(request, 'product/products.html', context=context)


def category(request, category_slug):
    cat = get_object_or_404(models.PhoneCategory, slug=category_slug)
    context = {'title': f'Product' + str(cat.name),
               'category': cat,
               }
    return render(request, 'product/category.html', context=context)


def products_for_year(request, year):
    if year > 2025:
        raise Http404()
        # return redirect('index')
    context = {'title': f'Products for {year}'}
    return HttpResponse('Products for year ' + str(year))


def product(request, product_slug):
    pr = get_object_or_404(PhoneProduct, slug=product_slug)
    context = {'title': f'Product' + str(pr.name),
               'product': pr,
               }
    return render(request, 'product/product_slug.html', context)


def add_product(request):
    if request.method == 'POST':
        form = forms.AddProductForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                PhoneProduct.objects.create(**form.cleaned_data)
                data = form.cleaned_data
                print(data)
                return redirect('index')
            except:
                print('Something went wrong')
                form.add_error(None, 'Error adding product')
    else:
        form = forms.AddProductForm()
    context = {'title': f'Product adding',
               'form': form,
               }
    return render(request, 'product/add_product.html', context=context)


def handler404(request, exception):
    return HttpResponseNotFound('Page not found :(')
