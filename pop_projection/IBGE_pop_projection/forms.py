from django import forms
from .models import Datas

class GeeksForm(forms.ModelForm):
    data = forms.DateField( )

    class Meta:
        model=Datas
        fields=('data',)
