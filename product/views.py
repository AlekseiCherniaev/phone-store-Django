from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, CreateView

from product import models
from product.models import PhoneProduct, PhoneTag
from product import forms
from product.utils import DataMixin


class IndexView(DataMixin, TemplateView):
    template_name = 'product/index.html'
    title_page = 'Main Page'
    # extra_context = {'title': 'Main Page'}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Main Page'
    #     return context


class AllProductsPageView(ListView):
    template_name = 'product/products.html'
    model = models.PhoneProduct
    context_object_name = 'products'
    paginate_by = 4
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


class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'product/add_product.html'
    form_class = forms.AddProductForm
    success_url = reverse_lazy('index')
    title_page = 'Add Product'


def handler404(request, exception):
    return HttpResponseNotFound('Page not found :(')
