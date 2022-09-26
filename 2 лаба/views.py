from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from bmstu_lab.models import Car

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Camry 3.5', 'id': 1},
            {'title': 'Lambo Urus', 'id': 2},
            {'title': 'Новый Мерин', 'id': 3},
        ]
    }})
def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

def carList(request):
    return render(request, 'cars.html', {'data' : {
        'current_date': date.today(),
        'cars': Car.objects.all()
    }})

def GetCar(request, id):
    return render(request, 'car.html', {'data' : {
        'current_date': date.today(),
        'book': Car.objects.filter(id=id)[0]
    }})
