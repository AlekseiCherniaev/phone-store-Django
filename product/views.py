from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from product import models
from product.models import PhoneProduct, PhoneTag
from product import forms
from product.utils import DataMixin


# def index(request):
#     context = {'title': 'Main Page'}
#     return render(request, 'product/index.html', context=context)


class IndexView(DataMixin, TemplateView):
    template_name = 'product/index.html'
    title_page = 'Main Page'
    # extra_context = {'title': 'Main Page'}

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


class AllProductsPageView(ListView):
    template_name = 'product/products.html'
    model = models.PhoneProduct
    context_object_name = 'products'
    paginate_by = 3
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
        if len(tags_list) == 0:
            products_ = models.PhoneProduct.phone_objects.all()
        else:
            products_ = models.PhoneProduct.phone_objects.filter(tag__tag__in=tags_list).distinct()
        return products_


# def category(request, category_slug):
#     cat = get_object_or_404(models.PhoneCategory, slug=category_slug)
#     context = {'title': f'Product' + str(cat.name),
#                'category': cat,
#                }
#     return render(request, 'product/category.html', context=context)


class ProductForCategory(DetailView):
    model = models.PhoneCategory
    template_name = 'product/category.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category '
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(models.PhoneCategory.objects, slug=self.kwargs[self.slug_url_kwarg])


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

# class AddProduct(View):
#     def get(self, request):
#         form = forms.AddProductForm()
#         context = {'title': f'Product adding',
#                    'form': form,
#                    }
#         return render(request, 'product/add_product.html', context=context)
#
#     def post(self, request):
#         form = forms.AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         context = {'title': f'Product adding',
#                    'form': form,
#                    }
#         return render(request, 'product/add_product.html', context=context)


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


class AddProduct(DataMixin, CreateView):
    template_name = 'product/add_product.html'
    form_class = forms.AddProductForm
    success_url = reverse_lazy('index')
    title_page = 'Add Product'


def handler404(request, exception):
    return HttpResponseNotFound('Page not found :(')
