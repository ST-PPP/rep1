from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
       model = Product
       fields = [
           'name',
           'description',
           'category',
           'price',
           'quantity',
       ]

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError('Название должно начинаться с заглавной буквы.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if description is not None and len(description) < 15:
            raise ValidationError('Описание не может быть менее 15 символов.')
        return description

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name == description:
            raise ValidationError('Описание не должно быть идентичным названию.')
        return cleaned_data
