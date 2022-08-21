from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def tarjetas(request):
    return render(request, "Tarjetas/tarjetas.html")