from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def cuentas(request):
    return render(request, "Cuentas/cuentas.html")