from django import forms

from app.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['ean_code', 'original_price', 'price', 'description']
