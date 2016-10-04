from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse
from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json
import urllib.request
import datetime
from currency.forms import InputValueForm
from django.core.urlresolvers import reverse_lazy
from currency.function import Currency_Setting


# When form is handled by django
class CurrencyIndexView(FormView):
    template_name = 'currency/index.html'
    success_url = reverse_lazy('currency:select')
    form_class = InputValueForm
    Currency_Setting().load_new_currency()

    def form_valid(self, form):
        form.submitted(self.request)
        return super(CurrencyIndexView, self).form_valid(form)

class SelectView(View):
    def post(self, request):
        form = InputValueForm(request.POST)

        if form.is_valid():
            used_amount = form.cleaned_data['used_amount_field']
            selected_currency = form.cleaned_data['select_currency_field']

            # lastcurrency is latest object of selected currency model
            lastcurrency = Currency_Setting().check_selected_currency(selected_currency)

            # check created date of latest object
            datecheck = Currency_Setting().check_created_date(lastcurrency)

            # if created date of latest object is today, then use latest object
            if datecheck == True:
                lastcurrency.currency_final = round(
                    CurrencyKRW.objects.last().currency_rate / lastcurrency.currency_rate, 2)
                lastcurrency.save()

            # if created date of latest object is not today, then load new currency data and reload latest object of selected currency model
            else:
                Currency_Setting().load_new_currency()
                lastcurrency = Currency_Setting().check_selected_currency(selected_currency)
                lastcurrency.currency_final = CurrencyKRW.objects.last().currency_rate / lastcurrency.currency_rate
                lastcurrency.save()

        used_amount_to_krw = int(lastcurrency.currency_final * used_amount)
        return render(request, 'currency/result.html',
                      {'currency': lastcurrency, 'used_amount_to_krw': used_amount_to_krw, 'used_amount': used_amount})

