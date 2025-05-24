from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contato(request):
    context = {
        'nome':'MotorWeb',
        'fone':'35621011',
        'email':'motor@motor.com.br',
    }
    return render(request,'contato.html',context)