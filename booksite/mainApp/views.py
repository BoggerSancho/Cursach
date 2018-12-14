from django.shortcuts import render
from .models import Books
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth import authenticate

def index(request):
    all_book = Books.objects.all()
    return render(request, 'mainApp/myindex.html', all_book)

def register(request):
    return render(request, 'mainApp/register.html')

class List(TemplateView):
    def get(self, request):
        all_book = Books.objects.all()
        # username = request.POST['username']
        # password = request.POST['password']
        # if username == 'bogger':
        #     template_name = 'mainApp/myindex.html'
        # else:
        #     template_name = 'mainApp/register.html'
        template_name = 'mainApp/myindex.html'
        ctx = {
            'all_book': all_book,
        }
        # print('Heoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
        # print(username)
        # print(password)

        return render(request, template_name, ctx)