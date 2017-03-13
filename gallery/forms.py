from django.forms import ModelForm
from .models import *

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'image']
