from django import forms
from currency.models import Choice
from django.shortcuts import render
from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP



class InputValueForm(forms.Form):
    used_amount_field = forms.IntegerField(label="Used Amount")
    choice_datas = Choice.objects.all()
    choice_list = []
    for choice in choice_datas:
        choice_list.append((choice, choice.choice_text))
    select_currency_field = forms.ChoiceField(choices=choice_list, widget=forms.Select(), label="Now Currency")

