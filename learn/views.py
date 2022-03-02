from django.shortcuts import render

# Create your views here.

def index(request):
    request.session['customerid'] = 1

    resellers=[
        {'companyregid':1, 'companyname':'baabte', 'country':'india', 'status':'Active'},

        {'companyregid':2, 'companyname':'TCS','country':'india', 'status':'Active'},

        {'companyregid':3, 'companyname':'UST','country':'india','status':'Active'},
    ]
    return render(request, 'index.html', {'resellerdata':resellers})










   



