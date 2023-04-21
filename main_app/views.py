from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stone

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
  return render(request, 'stones/detail.html', { 'stone': stone })

class StoneCreate(CreateView):
  model = Stone
  fields = '__all__'

class StoneUpdate(UpdateView):
  model = Stone
  fields = ['color', 'description']

class StoneDelete(DeleteView):
  model = Stone
  success_url = '/stones'