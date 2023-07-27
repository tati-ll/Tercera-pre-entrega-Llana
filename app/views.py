from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from app.models import Alumno, Taller, Material

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response

class AlumnoListView(ListView):
    model= Alumno
    template_name='app/lista_alumnos.html'

class TallerListView(ListView):
    model= Taller
    template_name='app/lista_talleres.html'

class MaterialListView(ListView):
    model= Material
    template_name='app/lista_materiales.html'

class AlumnoCreateView(CreateView):
    model= Alumno
    fields=('apellido', 'nombre', 'email')
    success_url= reverse_lazy('lista_alumnos')

class TallerCreateView(CreateView):
    model= Taller
    fields=('nombre', 'profesor', 'fecha', 'descripcion', 'cupos')
    success_url= reverse_lazy('lista_talleres')

class MaterialCreateView(CreateView):
    model= Material
    fields=('nombre', 'marca', 'color', 'composicion')
    success_url= reverse_lazy('lista_materiales')


def buscar_taller(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda", "")
        talleres = Taller.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "talleres": talleres,
            "busqueda": busqueda,
        }
        http_response = render(
            request=request,
            template_name='app/resultado_talleres.html',
            context=contexto,
        )
        return http_response
   return render(request, 'app/buscar_taller.html')