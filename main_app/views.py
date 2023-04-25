from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Stone, Villain
from .forms import UseForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stones_index(request):
    stones = Stone.objects.all()
    return render(request, 'stones/index.html', { 'stones': stones })

def stones_detail(request, stone_id):
  stone = Stone.objects.get(id=stone_id)
  id_list = stone.villains.all().values_list('id')
  villains_stone_doesnt_have = Villain.objects.exclude(id__in=id_list)
  use_form = UseForm()
  return render(request, 'stones/detail.html', { 
    'stone': stone,
    'use_form': use_form,
    'villains': villains_stone_doesnt_have
  })

class StoneCreate(CreateView):
  model = Stone
  fields = ['name', 'color', 'description']

class StoneUpdate(UpdateView):
  model = Stone
  fields = ['color', 'description']

class StoneDelete(DeleteView):
  model = Stone
  success_url = '/stones'
  
def add_use(request, stone_id):
  form = UseForm(request.POST)
  if form.is_valid():
    new_use= form.save(commit=False)
    new_use.stone_id = stone_id
    new_use.save()
  return redirect('detail', stone_id=stone_id)

class VillainList(ListView):
  model = Villain

class VillainDetail(DetailView):
  model = Villain

class VillainCreate(CreateView):
  model = Villain
  fields = '__all__'

class VillainUpdate(UpdateView):
  model = Villain
  fields = ['name']

class VillainDelete(DeleteView):
  model = Villain
  success_url = '/villains'

def assoc_villain(request, stone_id, villain_id):
  Stone.objects.get(id=stone_id).villains.add(villain_id)
  return redirect('detail', stone_id=stone_id)

def unassoc_villain(request, stone_id, villain_id):
  Stone.objects.get(id=stone_id).villains.remove(villain_id)
  return redirect('detail', stone_id=stone_id)
