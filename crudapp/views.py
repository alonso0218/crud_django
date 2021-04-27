from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EstudianteForm
from .models import Estudiante

#creamos las vistas que nos permitiran hacer el crud
# Create your views here.
def adicion(request):
    #estudiante=estudiante.objects.all()
    form = EstudianteForm(request.POST or None)
    if form.is_valid():
       form.save()
    return render(request,'adicion.html',{'form':form})

def show(request):
    estudiante=Estudiante.objects.all()
    return render(request,'show.html',{'estudiante':estudiante})


def update(request, id):
    estudiante=Estudiante.objects.get(id=id)
    form = EstudianteForm(request.POST,instance=estudiante)
    if form.is_valid():
       form.save()
       return HttpResponseRedirect("/")
    return render(request,'update.html',{'estudiante':estudiante})

def delete(request, id):
    form=Estudiante.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect("/")