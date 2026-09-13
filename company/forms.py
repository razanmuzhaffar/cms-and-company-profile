from django import forms
from .models import PesanKontak


class KontakForm(forms.ModelForm):
    class Meta:
        model = PesanKontak
        fields = ['nama', 'email', 'subjek', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Nama Anda'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email Anda'
            }),
            'subjek': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Subjek'
            }),
            'pesan': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Tulis pesan Anda...', 'rows': 5
            }),
        }
