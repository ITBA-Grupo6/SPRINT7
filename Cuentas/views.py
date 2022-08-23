from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def cuentas(request):
    if request.user.username:
        return render(request, "Cuentas/cuentas.html", {'name': request.user.username})
    else: 
        return render(request, "Cuentas/cuentas.html")