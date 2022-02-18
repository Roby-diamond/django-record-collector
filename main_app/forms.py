from django.forms import ModelForm
from .models import Market

class MarketForm(ModelForm):
    class Meta:
        model = Market
        fields = ['date', 'transaction']
