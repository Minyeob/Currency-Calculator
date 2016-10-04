from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP
import json
import urllib.request
import datetime


class Currency_Setting:
    # check what currency is selected
    def check_selected_currency(self, selected_currency):
        currencyModel_list = [CurrencyKRW.objects.last(), CurrencyEUR.objects.last(), CurrencyCNY.objects.last(),
                              CurrencyJPY.objects.last(), CurrencyGBP.objects.last()]
        selected_currency_model = currencyModel_list[0]
        for currencymodel in currencyModel_list:
            if currencymodel.title == selected_currency:
                selected_currency_model = currencymodel
        return selected_currency_model

    # check created date of latest object
    def check_created_date(self, lastcurrency):
        today = datetime.date.today()
        if lastcurrency.pub_date == datetime.date.today():
            return True
        else:
            return False

    # load new currency data
    def load_new_currency(self):
        currencyeur = CurrencyEUR()
        currencykrw = CurrencyKRW()
        currencycny = CurrencyCNY()
        currencyjpy = CurrencyJPY()
        currencygbp = CurrencyGBP()
        json_object = "https://openexchangerates.org/api/latest.json?app_id=548749f027434cde84582df98bb8df5b"
        recived_object = urllib.request.urlopen(json_object)
        # 2에서는 그냥 urlopen을 하고 read를 한 뒤 json load를 하면 가능하였지만 3에서는 json load는 str의 형태만 가능하므로
        # url을 통해 받아오고 read 한 파일을 decoding 해서 string으로 만들어 줘야 한다.
        url_str = recived_object.read()
        recived_data = json.loads(url_str.decode('utf-8'))
        currencyeur.currency_rate = float(recived_data["rates"]["EUR"])
        currencykrw.currency_rate = float(recived_data["rates"]["KRW"])
        currencycny.currency_rate = float(recived_data["rates"]["CNY"])
        currencyjpy.currency_rate = float(recived_data["rates"]["JPY"])
        currencygbp.currency_rate = float(recived_data["rates"]["GBP"])
        currencyeur.save()
        currencykrw.save()
        currencycny.save()
        currencyjpy.save()
        currencygbp.save()