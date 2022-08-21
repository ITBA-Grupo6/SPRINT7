from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def prestamos(request):
    if request.user.username:
        return render(request, "Prestamos/prestamos.html", {'name': request.user.username})
    else: 
        return render(request, "Prestamos/prestamos.html")