from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.forms import PosteForm
from .models import Poste


class ListePostes(ListView):
    model = Poste
    template_name = 'mag/Liste_Postes.html'
    context_object_name = 'Postes'


class DetailPoste(DetailView):
    model = Poste
    template_name = 'mag/detail_Poste.html'
    context_object_name = 'Poste'


class CreerPoste(CreateView):

    model = Poste

    template_name = 'mag/Creer_Poste.html'

    form_class = PosteForm

    success_url = reverse_lazy('Liste_Postes')


class ModifierPoste(UpdateView):

    model = Poste

    template_name = 'mag/Modifier_Poste.html'

    form_class = PosteForm

    success_url = reverse_lazy('Liste_Postes')


class SupprimerPoste(DeleteView):

    model = Poste

    template_name = 'mag/supprimer_Poste.html'
    success_url = reverse_lazy('Liste_Postes')
