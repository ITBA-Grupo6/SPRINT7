from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.username:
        return render(request, "Base/home.html", {'name': request.user.username})
    else:
        return render(request, "Base/home.html")

def registro(request):
    return render(request, "Base/registro.html")