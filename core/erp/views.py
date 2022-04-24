from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def myfirstview(request):
    data = {
        'name': 'william',
        'categories': Category.objects.all()
    }
    # return HttpResponse('hola esta es mi  primera url')
    # return JsonResponse(data)
    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name': 'william',
        'products': Product.objects.all()
    }
    # return HttpResponse('hola esta es mi  primera url')
    # return JsonResponse(data)
    return render(request, 'second.html', data)
