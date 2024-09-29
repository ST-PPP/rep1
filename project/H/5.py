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

    def clean(self): # Мы переопределили метод clean и реализовали в нём проверку.
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "description": "Описание не может быть менее 20 символов."
            })

        name = cleaned_data.get("name")
        if name == description:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data