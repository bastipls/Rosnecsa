from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/',views.logout_view, name="logout"),
    path('login/registro_inicial/',views.registro_inicial,name='registro_inicial'),
    path('listar_clientes/',views.listar_clientes, name='listar_clientes'),
    path('crear_folio/',views.crear_folio, name='crear_folio'),
]