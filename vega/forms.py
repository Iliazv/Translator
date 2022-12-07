from django import forms
from .models import Document


#MyImage = ImageClass()

class UploadFile(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)