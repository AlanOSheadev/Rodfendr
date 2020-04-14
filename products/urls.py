from django.conf.urls import url, include
from .views import all_products, description

urlpatterns =[
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', description, name='description'),
]
