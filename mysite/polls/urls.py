from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserLogin, name='UserLogin'),

    # path('add_news', views.add_news, name='add_news')

]
