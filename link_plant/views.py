from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    template_name = 'link_plant/link_list.html'
    context_object_name = 'links'   # default is object_list
    
class LinkCreateView(CreateView):
    model = Link
    template_name = 'link_plant/link_create.html'
    fields = "__all__"
    success_url = reverse_lazy('link_list')
    