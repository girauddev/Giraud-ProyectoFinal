from django.urls import path
from . import views

urlpatterns = [
    path('form_page/', views.CreatePage.as_view(), name='pageForm'),
    path('list_page/', views.ListPage.as_view(), name='pageList'),
    path('delete_page/<pk>/', views.DeletePage.as_view(), name='pageDelete'),
    path('pages/<pk>/', views.ViewPage.as_view(), name='pageDetail'),
    path('update_page/<pk>/', views.UpdatePage.as_view(), name='pageUpdate'),

]