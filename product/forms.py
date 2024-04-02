from django import forms
from django.core import validators
from django.utils.deconstruct import deconstructible

from product import models


@deconstructible
class RussianNameValidator:
    ALLOWED_CHARS = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю1234567890-_'
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны быть русские буквы'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise forms.ValidationError(self.message, code=self.code)


class AddProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=models.PhoneCategory.objects.all(), label='Made by')

    class Meta:
        model = models.PhoneProduct
        # fields = '__all__'
        fields = ['name', 'price', 'quantity', 'description', 'image', 'slug', 'category', 'tag']
        labels = {'name': 'Phone Name', 'category': 'Phone category', 'price': 'Phone price', 'image': 'Phone image',
                  'description': 'Phone description', 'quantity': 'Phone quantity', 'tag': 'Phone tag',
                  'slug': 'Phone slug'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-input'}),
                   'description': forms.Textarea(attrs={'cols': 50, 'rows': 5})}

    # tag = forms.ModelChoiceField(queryset=models.PhoneTag.objects.all(), required=False, label='Tags')

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     ALLOWED_CHARS = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю1234567890-_'
    #
    #     if not (set(name) <= set(ALLOWED_CHARS)):
    #         raise forms.ValidationError('Должны быть русские буквы')
