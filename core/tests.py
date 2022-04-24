from config.wsgi import *
from django.test import TestCase
from core.erp.models import Type

# Create your tests here.
# Listar
# query = Type.objects.all()
# print(query)

# insercion
# t = Type(name = 'Pruebalala').save()


#edicion
# try:
#     L = Type.objects.get(pk=1)
#     L.name = 'AccionistaM'
#     L.save()
# except Exception as e:
#     print(e)
#     print(L.name)

# obj = Type.objects.filter(name__contains='pre')
# obj = Type.objects.filter(name__istartswith='p').count()
# obj = Type.objects.filter(name__istartswith='p')
# obj = Type.objects.filter(name__istartswith='p').exclude(id=5)
# obj = Type.objects.filter(name__iendswith='a').exclude(id=5)

for i in Type.objects.filter(name__contains='a')[:2]:
    print(i.name)


# print(obj)