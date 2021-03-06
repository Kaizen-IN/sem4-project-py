from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('login/',views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('register/', views.register_view, name = "register"),
    path('home/', views.home, name = "home"),
]