from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from product import models
from product.models import PhoneProduct, PhoneTag
from product import forms


# def index(request):
#     context = {'title': 'Main Page'}
#     return render(request, 'product/index.html', context=context)


class IndexView(TemplateView):
    template_name = 'product/index.html'
    extra_context = {'title': 'Main Page'}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Main Page'
    #     return context


# def products(request):
#     # list of selected tags
#     tags_list = []
#     for tag in PhoneTag.objects.all():
#         if tag.tag in request.GET:
#             tags_list.append(tag.tag)
#     # if none of tags are selected or all are selected
#     if len(tags_list) == 0 or len(tags_list) == models.PhoneTag.objects.count():
#         products_ = models.PhoneProduct.phone_objects.all()
#     else:
#         products_ = models.PhoneProduct.objects.filter(tag__tag__in=tags_list).distinct()
#
#     context = {'title': 'Products',
#                'products': products_,
#                'categories': models.PhoneCategory.objects.all(),
#                'tags': PhoneTag.objects.all(),
#                }
#     return render(request, 'product/products.html', context=context)


class ProductsView(ListView):
    template_name = 'product/products.html'
    model = models.PhoneProduct
    context_object_name = 'products'

    extra_context = {'title': 'Products',
                     'categories': models.PhoneCategory.objects.all(),
                     'tags': PhoneTag.objects.all(),
                     }

    def get_queryset(self):
        # list of selected tags
        tags_list = []
        for tag in PhoneTag.objects.all():
            if tag.tag in self.request.GET:
                tags_list.append(tag.tag)
        # if none of tags are selected or all are selected
        if len(tags_list) == 0 or len(tags_list) == models.PhoneTag.objects.count():
            products_ = models.PhoneProduct.phone_objects.all()
        else:
            products_ = models.PhoneProduct.objects.filter(tag__tag__in=tags_list).distinct()
        return products_


# def category(request, category_slug):
#     cat = get_object_or_404(models.PhoneCategory, slug=category_slug)
#     context = {'title': f'Product' + str(cat.name),
#                'category': cat,
#                }
#     return render(request, 'product/category.html', context=context)


class ProductForCategory(ListView):
    model = models.PhoneCategory
    template_name = 'product/category.html'
    context_object_name = 'category'

    def get_queryset(self):
        print(self.kwargs['category_slug'])
        print(models.PhoneCategory.objects.filter(slug=self.kwargs['category_slug']))
        return models.PhoneCategory.objects.filter(slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['category'][0]
        context['title'] = 'Category ' + str(cat.name)
        context['category'] = cat

        return context


def products_for_year(request, year):
    if year > 2025:
        raise Http404()
        # return redirect('index')
    context = {'title': f'Products for {year}'}
    return HttpResponse('Products for year ' + str(year))


# def product(request, product_slug):
#     pr = get_object_or_404(PhoneProduct, slug=product_slug)
#     context = {'title': f'Product' + str(pr.name),
#                'product': pr,
#                }
#     return render(request, 'product/product_slug.html', context)


class ProductView(DetailView):
    model = PhoneProduct
    template_name = 'product/product_slug.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pr = models.PhoneProduct.objects.filter(slug=self.kwargs['product_slug']).first()
        context['title'] = f'{pr.name}'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(PhoneProduct.phone_objects, slug=self.kwargs[self.slug_url_kwarg])


# def add_product(request):
#     if request.method == 'POST':
#         form = forms.AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = forms.AddProductForm()
#     context = {'title': f'Product adding',
#                'form': form,
#                }
#     return render(request, 'product/add_product.html', context=context)

class AddProduct(View):
    def get(self, request):
        form = forms.AddProductForm()
        context = {'title': f'Product adding',
                   'form': form,
                   }
        return render(request, 'product/add_product.html', context=context)

    def post(self, request):
        form = forms.AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'title': f'Product adding',
                   'form': form,
                   }
        return render(request, 'product/add_product.html', context=context)


def handler404(request, exception):
    return HttpResponseNotFound('Page not found :(')
