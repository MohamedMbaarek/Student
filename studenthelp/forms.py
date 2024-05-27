from django import forms
from .models import Post, Transport

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'type', 'date', 'titre', 'contenu', 'statut']

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['depart', 'destination', 'heure_dep', 'nbre_sieges', 'contactinfo', 'club', 'prix']
