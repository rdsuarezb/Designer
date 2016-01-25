from django.shortcuts import render
from django.http import *
import datetime
from web.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/Perfil")
    else:
        # Show an error page
        return HttpResponseRedirect("/")

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")
    
def CargarPrincipal(request):
    return render(request, 'Principal.html', {})

def CargarPerfil(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'Perfil.html', {})

def CargarDocumentos(request):
    return render(request, 'Documentos.html', {})

def CargarAreaDeTrabajo(request):
    return render(request, 'AreaDeTrabajo.html', {})


