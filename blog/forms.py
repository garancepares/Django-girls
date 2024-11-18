from django import forms
 
from .models import Livre
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Livre
        fields = ('lieu',)