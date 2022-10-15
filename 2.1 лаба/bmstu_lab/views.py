from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from bmstu_lab.models import cars, tx, user

def hello(request):
    return HttpResponse('Hello world!')

def hello(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

'''def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'hotels': GetData()
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'hotels': GetData()

    }}) '''

'''def bookList(request):
    return render(request, 'books.html', {'data' : {
        'current_date': date.today(),
        'books': Book.objects.all()
    }}) '''

def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'orders': [
            {'id': 1, 'title': 'Mirror House South', 'release date': '17.09.2021','developer': 'Crytek', 'publisher': 'Crytek'},
            {'id': 2, 'title': 'Villa Korcula Diamond'},
            {'id': 3, 'title': 'Villa Richard Meier'},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'id': id
    }})

def carList(request):
    return render(request, 'cars.html', {'data' : {
        'current_date': date.today(),
        'cars': cars.objects.all()
    }})

def Getcars(request, id):
    return render(request, 'car.html', {'data' : {
        'current_date': date.today(),
        'car': cars.objects.filter(id=id)[0]
    }})

def Alltx(request):
    return render(request, 'tx.html', {'data' : {
        'current_date': date.today(),
        'tx': tx.objects.all()
    }})

def Gettx(request, id):
    return render(request, 'tx.html', {'data' : {
        'current_date': date.today(),
        'tx': tx.objects.filter(id=id)[0]
    }})

def userList(request):
    return render(request, 'user.html', {'data' : {
        'current_date': date.today(),
        'user': user.objects.all()
    }})

def Getuser(request, id):
    return render(request, 'user.html', {'data' : {
        'current_date': date.today(),
        'user': user.objects.filter(id=id)[0]
    }})