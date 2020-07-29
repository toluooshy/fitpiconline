import os
import platform
import getpass
import random
from django.core.management import call_command
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# VIEWS:

def index(request):
    call_command('makemigrations')
    call_command('migrate')
    return render(request, 'herokuapp/index.html')

def outfit(request):
    call_command('makemigrations')
    call_command('migrate')
    if (len(Clothing.objects.all().filter(category='TOPS')) == 0):
        tops = '<try adding something here/>'
    else:
        tops = random.choice(Clothing.objects.all().filter(category='TOPS'))
    
    if (len(Clothing.objects.all().filter(category='BTTM')) == 0):
        bottoms = '<try adding something here/>'
    else:
        bottoms = random.choice(Clothing.objects.all().filter(category='BTTM'))

    if (len(Clothing.objects.all().filter(category='FTGR')) == 0):
        footgear = '<try adding something here/>'
    else:
        footgear = random.choice(Clothing.objects.all().filter(category='FTGR'))

    if (len(Clothing.objects.all().filter(category='HDGR')) == 0):
        headgear = '<try adding something here/>'
    else:
        headgear = random.choice(Clothing.objects.all().filter(category='HDGR'))

    if (len(Clothing.objects.all().filter(category='ACCS')) == 0):
        accessories = '<try adding something here/>'
    else:
        accessories = random.choice(Clothing.objects.all().filter(category='ACCS'))
    content = {
        'tops':tops,
        'bottoms':bottoms,
        'footgear':footgear,
        'headgear':headgear,
        'accessories':accessories
    }
    return render(request, 'herokuapp/outfit.html', content)

def inventory(request):
    call_command('makemigrations')
    call_command('migrate')
    clothes = Clothing.objects.all()

    form = ClothingForm()

    if request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/inventory')

    context = {'clothes':clothes, 'form':form}
    return render(request, 'herokuapp/inventory.html', context)

def about(request):
    call_command('makemigrations')
    call_command('migrate')
    return render(request, 'herokuapp/about.html')

def updateClothing(request, pk):
    call_command('makemigrations')
    call_command('migrate')
    clothes = Clothing.objects.get(id=pk)
    item = Clothing.objects.get(id=pk)

    form = ClothingForm(instance=clothes)

    if request.method == 'POST':
        form = ClothingForm(request.POST, instance=clothes)
        if form.is_valid():
            form.save()
            return redirect('/inventory')

    context = {'form':form, 'item':item}

    return render(request, 'herokuapp/updateclothing.html', context)

def deleteClothing(request, pk):
    call_command('makemigrations')
    call_command('migrate')
    item = Clothing.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/inventory')

    context = {'item':item}
    return render(request, 'herokuapp/deleteclothing.html', context)