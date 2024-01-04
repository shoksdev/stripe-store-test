from django import forms

from .models import Order, Item


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Order
        fields = ('items', )
