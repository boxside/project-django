from django import forms
from .models import Parameter

class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ['amount']  # Hanya 'amount' yang bisa diubah