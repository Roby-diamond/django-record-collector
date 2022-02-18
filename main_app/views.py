from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record, Genre
from .forms import MarketForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    genres_record_doesnt_have = Genre.objects.exclude(id__in = record.genres.all().values_list('id'))
    market_form = MarketForm()
    return render(request,'records/detail.html',{
        'record': record, 'market_form': market_form,
        'genres': genres_record_doesnt_have
    })

def add_market(request, record_id):
    form = MarketForm(request.POST)
    if form.is_valid():
        new_market = form.save(commit=False)
        new_market.record_id = record_id
        new_market.save()
    return redirect('detail', record_id=record_id)

def assoc_genre(request, record_id, genre_id):
    Record.objects.get(id=record_id).genres.add(genre_id)
    return redirect('detail', record_id=record_id)

class RecordCreate(CreateView):
    model = Record
    fields = ('title', 'artist', 'release_date')

class RecordUpdate(UpdateView):
    model = Record
    fields = ('artist', 'release_date')

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

class GenreCreate(CreateView):
    model = Genre
    fields = ('name',)

class GenreUpdate(UpdateView):
    model = Genre
    fields = ('name',)

class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres/'

class GenreDetail(DetailView):
    model = Genre
    template_name = 'genres/detail.html'

class GenreList(ListView):
    model = Genre
    template_name = 'genres/index.html'