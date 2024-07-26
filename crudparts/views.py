from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Crudparts


class CrudpartsListView(ListView):
    model = Crudparts


class CrudpartsCreateView(CreateView):
    model = Crudparts
    fields = ["cod", "description", "equipamento"]
    success_url = reverse_lazy("crudparts_list")


class CrudpartsDeleteView(DeleteView):
    model = Crudparts
    success_url = reverse_lazy("crudparts_list")
