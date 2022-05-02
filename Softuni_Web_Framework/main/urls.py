from django.urls import path

from Softuni_Web_Framework.main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]