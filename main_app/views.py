from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stone
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
  use_form = UseForm()
  return render(request, 'stones/detail.html', { 
    'stone': stone,
    'use_form': use_form
  })

def add_use(request, stone_id):
  form = UseForm(request.POST)
  if form.is_valid():
    new_use= form.save(commit=False)
    new_use.stone_id = stone_id
    new_use.save()
  return redirect('detail', stone_id=stone_id)

class StoneCreate(CreateView):
  model = Stone
  fields = '__all__'

class StoneUpdate(UpdateView):
  model = Stone
  fields = ['color', 'description']

class StoneDelete(DeleteView):
  model = Stone
  success_url = '/stones'