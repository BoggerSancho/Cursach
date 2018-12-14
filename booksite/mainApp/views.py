from django.shortcuts import render
from .models import Books
from django.views.generic import ListView, DetailView, TemplateView

def index(request):
    all_book = Books.objects.all()
    return render(request, 'mainApp/myindex.html', all_book)

def register(request):
    return render(request, 'mainApp/register.html')

class List(TemplateView):
    template_name = 'mainApp/myindex.html'
    def get(self, request):
        all_book = Books.objects.all()

        ctx = {
            'all_book': all_book,
        }

        return render(request, self.template_name, ctx)