from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record
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
    market_form = MarketForm()
    return render(request,'records/detail.html',{
        'record': record, 'market_form': market_form
    })

def add_market(request, record_id):
    form = MarketForm(request.POST)
    if form.is_valid():
        new_market = form.save(commit=False)
        new_market.record_id = record_id
        new_market.save()
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