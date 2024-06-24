from django import forms
from django.db.models import ForeignKey, ManyToManyField
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Discount
#


class DiscountForm(ModelForm):

    class Meta:
        model = Discount
        fields = ['title', 'description', 'company', 'sales', 'sale_date_start', 'sale_date_end', 'status', 'tags']

        # widgets = {
        #     "title": TextInput(attrs={
        #         'placeholder': 'название акции'
        #     }),
        #     "description": Textarea(attrs={
        #         'placeholder': 'описание акции'
        #     }),
        #     "company": ForeignKey(attrs={
        #         'placeholder': 'компания'
        #     }),
        #     "categories": ForeignKey(attrs={
        #         'placeholder': 'категория'
        #     }),
        #     "sales": ForeignKey(attrs={
        #         'placeholder': 'предложение'
        #     }),
        #     "sale_date_start": DateTimeInput(attrs={
        #         'placeholder': 'начало акции'
        #     }),
        #     "sale_date_end": DateTimeInput(attrs={
        #         'placeholder': 'конец акции'
        #     }),
        #     "status": ForeignKey(attrs={
        #         'placeholder': 'статус акции'
        #     }),
        #     "tags": ManyToManyField(attrs={
        #         'placeholder': 'тэг'
        #     }),
        # }
    # renewal_date = forms.ChaarField(help_text="Название акции")