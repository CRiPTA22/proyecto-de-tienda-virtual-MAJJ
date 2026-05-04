from django.urls import path
from . import views

urlpatterns = [
    # 🟢 REGISTRO (página principal)
    path('', views.registro, name='registro'),

    # 🔐 LOGIN
    path('login/', views.login_view, name='login'),

    # 🏠 INICIO (página en blanco azul)
    path('inicio/', views.inicio, name='inicio'),

    # 🔓 LOGOUT (opcional pero recomendado 🔥)
    path('logout/', views.logout_view, name='logout'),
]