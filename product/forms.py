from django import forms
from django.forms import fields
from .models import FileUpload
class UploadForm(forms.ModelForm):
    title =  forms.CharField(max_length=100)
    doc_file = forms.FileField()
    image_file = forms.ImageField()

    class Meta:
        model = FileUpload
        fields = ['title', 'doc_file', 'image_file']