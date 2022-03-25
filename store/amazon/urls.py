from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('main',views.main,name="main"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name='logout')
]