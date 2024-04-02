from django import forms

from product import models


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=120, min_length=4, label='Product Name',
                           widget=forms.TextInput(attrs={'class': 'form-input'}),
                           error_messages={'required': 'Name is required',
                                           'min_length': 'Min length is 4'})
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50, }), label='About Phone')
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Price')
    category = forms.ModelChoiceField(queryset=models.PhoneCategory.objects.all(), label='Made by')
    image = forms.ImageField(required=False, label='Image')
    quantity = forms.IntegerField(required=False, label='Quantity')
    slug = forms.SlugField(max_length=120, label='Slug')
    # tag = forms.ModelChoiceField(queryset=models.PhoneTag.objects.all(), required=False, label='Tags')
