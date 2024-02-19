from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import movieform
from movieapp.models import movie


# Create your views here.

def index(req,):
    moviename=movie.objects.all()
    context={
        'movie_list':moviename
    }
    return render(req,"index.html",context)

def detail(req,movie_id):
    moviedetails=movie.objects.get(id=movie_id)
    return render(req,"details.html",{'moviedetails':moviedetails})

def add_movie(req):
    if req.method=="POST":
        name=req.POST.get('name')
        desc=req.POST.get('desc')
        year=req.POST.get('year')
        image=req.FILES['image']
        dir=req.POST.get('director')
        pro=req.POST.get('producer')
        lan=req.POST.get('language')
        adding_data=movie(name=name,desc=desc,year=year,image=image,director=dir,producer=pro,language=lan)
        adding_data.save()
    return render(req,"add_data.html")


def update(req,id):
    movie1=movie.objects.get(id=id)
    form=movieform(req.POST or None, req.FILES, instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(req,"edit.html",{'form':form,'movie1':movie1})


def delete(req,id):
    if req.method=="POST":
        movie2=movie.objects.get(id=id)
        movie2.delete()
        return redirect('/')
    return render(req,"delete.html")

