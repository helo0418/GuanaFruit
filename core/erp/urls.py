
from django.urls import path
from core.erp.views.insumo.views import *

app_name = 'erp'

urlpatterns = [

    path('insumo/list/', InsumoListView.as_view(), name='insumo_list'),
    path('insumo/add/', InsumoCreateView.as_view(), name='insumo_create'),

]