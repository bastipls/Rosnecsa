from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'),
   path('login/registro_inicial/',views.registro_inicial,name='registro_inicial'),
   path('logout/',views.logout_view, name="logout"),
   path('crear_folio/',views.crear_folio, name='crear_folio'),

]