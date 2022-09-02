from core.erp.models import *


data = ['leche' , 'azucar', 'leche condensada']

for i in data:
    ins = Insumo(name=i)
    ins.save()
    print('Guardado registro N{}'.format(ins.id))
