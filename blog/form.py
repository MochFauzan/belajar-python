from django.forms import ModelForm
from blog.models import Artikel

class FormTambahArtikel(ModelForm):
    class Meta:
        model = Artikel
        fields = '__all__'