from django import forms
from .models import Soru

class SoruForm(forms.ModelForm):
    class Meta:
        model = Soru
        fields = ['baslik', 'icerik']
