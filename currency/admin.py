from django.contrib import admin
from currency.models import CurrencyEUR, CurrencyCNY, CurrencyGBP, CurrencyJPY, CurrencyKRW, Choice

admin.site.register(CurrencyKRW)
admin.site.register(CurrencyEUR)
admin.site.register(CurrencyCNY)
admin.site.register(CurrencyGBP)
admin.site.register(CurrencyJPY)
admin.site.register(Choice)