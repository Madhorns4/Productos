from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'index.html')


class Listado(ListView):
    model = Usuario
    template_name = 'listado.html'
    queryset = Usuario.objects.filter(estado = 1)


class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'crear.html'
    success_url = reverse_lazy('usuario:listado')


class ActualizarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'crear.html'
    success_url = reverse_lazy('usuario:listado')


class EliminarUsuario(DeleteView):
    model = Usuario

    def post(self, request, pk, *args, **kwargs):
        object = Usuario.objects.get(user_id = pk)
        object.estado = 2
        object.save()
        return redirect('usuario:listado')


