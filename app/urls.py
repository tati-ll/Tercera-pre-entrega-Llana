from django.urls import path

from app.views import inicio, AlumnoListView, TallerListView, MaterialListView, AlumnoCreateView, TallerCreateView, MaterialCreateView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("alumnos/", AlumnoListView.as_view(), name="lista_alumnos"),
    path('talleres/', TallerListView.as_view(), name="lista_talleres"),
    path("materiales/", MaterialListView.as_view(), name="lista_materiales"),
    path("crear-alumno/", AlumnoCreateView.as_view(), name="crear_alumno"),
    path("crear-taller/", TallerCreateView.as_view(), name="crear_taller"),
    path("crear-material/", MaterialCreateView.as_view(), name="crear_material"),
]