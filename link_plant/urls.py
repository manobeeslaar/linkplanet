from django.urls import path

from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView

urlpatterns = [
    path("", LinkListView.as_view(), name="link_list"),
    path("link/create/", LinkCreateView.as_view(), name="link_create"),
    path("link/<int:pk>/update/", LinkUpdateView.as_view(), name="link_update"),
    path("link/<int:pk>/delete/", LinkDeleteView.as_view(), name="link_delete"),
]