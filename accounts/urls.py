from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/singup/', views.Register, name="register"),
    path('accounts/login/', views.Login, name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name="core/index.html"), name='logout'),
    path('accounts/profile/', views.Editar, name='editar'),
    path('accounts/avatares/', views.UserAvatar, name='avatar'),
    path('messages/', views.ListaMensajes.as_view(), name='ListaMensajes'),
    path('messages/send/', views.CrearMensajes.as_view(), name='CrearMensajes')
]