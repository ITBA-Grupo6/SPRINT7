from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistroForm


# Create your views here.
def home(request):
    if request.user.username:
        return render(request, "Base/home.html", {'name': request.user.username})
    else:
        return render(request, "Base/home.html")

def registro(request):

    registro_form = RegistroForm
    if request.method == "POST":
        registro_form = registro_form(data=request.POST)
        cliente_id= request.POST.get('cliente_id','')
        email = request.POST.get('email','')
        pwd = request.POST.get('pwd','')
        print(cliente_id,email,pwd)
        user = User.objects.create_user(cliente_id, email, pwd)
        user.save()
        print('creado')
        return redirect(reverse('login'))
    return render(request, "Base/registro.html")