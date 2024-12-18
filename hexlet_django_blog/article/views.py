from django.shortcuts import render

# Create your views here.
def index(request):
    tags = 'Главная страница article'
    return render(request, 'articles/index.html', context={'tags': tags},)