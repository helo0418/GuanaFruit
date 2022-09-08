
from django.urls import path
from core.erp.views.insumo.views import *

app_name = 'erp'




urlpatterns = [

    path('insumo/list/', InsumoListView.as_view(), name='insumo_list'),
    path('insumo/add/', InsumoCreateView.as_view(), name='insumo_create'),
    path('insumo/edit/<int:pk>/', InsumoUpdateView.as_view(), name='insumo_update'),
    path('insumo/delete/<int:pk>/', InsumoDeleteView.as_view(), name='insumo_delete')


]