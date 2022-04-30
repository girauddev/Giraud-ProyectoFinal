from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *

# Create your views here.
@login_required
def PageFormulario(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            msj = form.cleaned_data['title']   
            page = Page(title=data ['title'], content=data['content'], texto=data['texto'], usuario=data['usuario'])
            page.save()
            return render(request, "core/index.html", {'msj':f'Se creo la página "{msj}"'})
        else:
            return render(request, "pages/form_page.html", {'form':form})
    else:     
        form = PageForm()
        return render(request, "pages/form_page.html", {'form':form})

def ListPage(request):
    searchPage = request.GET.get('title', None)

    if searchPage is not None:
        pages = Page.objects.filter(title__icontains=searchPage)
    else:
        pages = Page.objects.all()
    form = SearchPage()
    return render(request, "pages/list_page.html", {'form':form,'pages':pages})

class DeletePage(DeleteView):
   model = Page
   success_url = '/list_page/'

class DetailPage(DetailView):
    model = Page
    template_name = 'pages/detail_page.html'