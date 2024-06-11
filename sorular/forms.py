from django import forms
from .models import Soru

class SoruForm(forms.ModelForm):
    class Meta:
        model = Soru
        fields = ['baslik', 'icerik']
        widgets = {
            'baslik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık'}),
            'icerik': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'İçerik'}),
        }
