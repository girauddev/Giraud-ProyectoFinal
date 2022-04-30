from django.urls import path
from . import views

urlpatterns = [
    path('form_page/', views.PageFormulario, name='pageForm'),
    path('list_page/', views.ListPage, name='pageList'),
    path('delete_page/<pk>/', views.DeletePage.as_view(), name='pageDelete'),
    path('pages/<pk>/', views.DetailPage.as_view(), name='pageDetail'),
]