from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


def test(request):
    return HttpResponse("<h4>Успешно</h4>")