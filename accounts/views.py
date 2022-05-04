from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.
def Register(request): 
    if request.method == 'POST':
        form = form_register(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "core/index.html", {'msj':f'Se creo el user {username}'})
        else:
            return render(request, "accounts/register.html", {'form':form})
    form = form_register()
    return render(request, "accounts/register.html", {'form':form})

def Login(request): 
    if request.method == 'POST':   
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not  None:
                login(request, user)
                usuario = form.cleaned_data['username']
                return render(request, "core/index.html", {'msj':f'Bienvenido {usuario}!'})
            else:
                return render(request, 'accounts/login.html', {'form':form},)
        else:
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

@login_required
def Editar(request):
    if request.method == 'POST':
        form = form_edit_user(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name','')
            logued_user.last_name = data.get('last_name','')
            if data.get('password1') == data.get('password2') and len(data.get("password1")) > 8:
                logued_user.set_password(data.get('password1'))
                msj = 'Se actualizo la contraseña'
            else:
                msj = 'No se cambio la contraseña'
            logued_user.save()
            return render(request, "core/index.html", {'msj':msj})
        else:
            return render(request, "accounts/user_edit.html", {'form':form, 'msj':''})
    form = form_edit_user(
        initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }
    )
    return render(request, "accounts/user_edit.html", {'form':form, 'msj':''})

@login_required
def UserAvatar(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)

    if len(avatares) > 0:
        return render(request, 'accounts/avatares.html', {"img":avatares[0].imagen.url})
    else:
        return render(request, 'accounts/avatares.html', {"msj":'Aún no tienes un avatar'})

class ListaMensajes(ListView):
    model = Mensaje
    template_name = '/accounts/mensaje_list.html'
    ordering = ['-created']

class CrearMensajes(CreateView):
    model = Mensaje
    form_class = CrearMensaje
    success_url = "/messages/"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'ctx': 'Enviar mensaje'
        })
        return ctx