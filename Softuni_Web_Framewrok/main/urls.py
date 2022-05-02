from django.urls import path

from Softuni_Web_Framewrok.main.views import IndexView

urlpatterns = [
    path('home/', IndexView.as_view(), name='index')
]