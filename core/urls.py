from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include("pages.urls")),
    path('accounts/', include("accounts.urls")),
    path('', views.Inicio, name="index"),
    path('about/', views.AboutUs.as_view(), name="about"),
    path('pages/',views.Blog, name="pages"),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout')
]