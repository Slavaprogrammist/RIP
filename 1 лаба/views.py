from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

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