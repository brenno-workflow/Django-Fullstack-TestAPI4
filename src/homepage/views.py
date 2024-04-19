from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import HomePageContent

def home(request):
    
    # Recuperar os dados da página inicial do banco de dados
    content = HomePageContent.objects.first()  # Assumindo que haja apenas uma entrada na tabela

    return render(request, 'homepage/home.html', {'content': content})
