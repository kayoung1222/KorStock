from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name='base'),
    path('news', views.news, name='news'),
    path('money', views.money, name='money'),
]

