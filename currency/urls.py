from django.conf.urls import url
from currency import views

urlpatterns = [
    url(r'^$', views.CurrencyIndexView.as_view(), name='index'),
    url(r'^select/$', views.SelectView.as_view(), name='select'),
    ]