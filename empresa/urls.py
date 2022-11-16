from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name="home_redirect"),
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
    path('empresas/', views.empresas, name="empresa"),
    path('empresas/excluir_empresa/id=<int:id>',
         views.excluir_empresa, name="excluir_empresa"),
    path('empresas/id=<int:id>', views.empresa, name="empresa_unica"),
]
