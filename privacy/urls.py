from django.conf.urls import url
from .views import privacy

urlpatterns = [
    url(r'^$', privacy, name='privacy'),
]
