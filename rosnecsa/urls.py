from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/',views.logout_view, name="logout"),
    path('login/registro_inicial/',views.registro_inicial,name='registro_inicial'),
    path('login/registro_inicial/error',views.error , name="error"),
    path('listar_clientes/',views.listar_clientes, name='listar_clientes'),
    path('crear_folio/',views.crear_folio, name='crear_folio'),
    path('listar_tecnicos/',views.listar_tecnicos, name= 'listar_tecnicos'),
    path('listar_tecnicos/<str:pk>/asignar_cliente',views.asignar_cliente, name="asignar_cliente"),
    path('crear_cliente/',views.crear_cliente,name="crear_cliente") 
]