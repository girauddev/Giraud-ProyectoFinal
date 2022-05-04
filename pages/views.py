from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import *
from .models import *

# Create your views here.
class ListPage(ListView):
    model = Page
    template_name = 'pages/list_page.html'
    ordering = ['-created']

class ViewPage(DetailView):
    model = Page
    template_name = 'pages/detail_page.html'
class CreatePage(CreateView):
    model = Page
    form_class = PageForm
    success_url = "/pages/"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({'msj': 'Crear post'})
        return ctx
class UpdatePage(UpdateView):
    model = Page
    form_class = PageForm
    success_url = "/pages/"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({'msj': 'Actualizar post'})
        return ctx
class DeletePage(DeleteView):
    model = Page
    success_url = "/pages/"
