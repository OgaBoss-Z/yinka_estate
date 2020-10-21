from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
   properties = Properties.objects.filter(is_featured=True).order_by('?')
   context = {
      'properties':properties,
   }
   return render(request, 'yinka/home.html', context)

def about(request):
   context = {}
   return render(request, 'yinka/about.html', context)

def contact(request):
   context = {}
   return render(request, 'yinka/contact.html', context)

def properties(request):
   properties = Properties.objects.all()
   context = {
      'properties':properties,
   }
   return render(request, 'yinka/properties.html', context)


def detail(request, pk, slug):
   properties = Properties.objects.get(pk=pk)
   images = PropertyImage.objects.filter(properties_id=pk)
   context= {
      'properties':properties,
      'images':images
   }
   return render(request, 'yinka/detail.html', context)

