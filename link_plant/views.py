from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
    
class LinkUpdateView(UpdateView):
    model = Link
    template_name = 'link_plant/link_create.html'
    fields = ['text', 'url']
    success_url = reverse_lazy('link_list')

class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'link_plant/link_delete.html'
    success_url = reverse_lazy('link_list')  
    cancel_url = reverse_lazy('link_list')
    
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links= profile.links.all()
    context = {
        'profile': profile,
        'links': links,
    }
    return render(request, 'link_plant/profile.html', context)
    