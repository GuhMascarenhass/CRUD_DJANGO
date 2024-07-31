from django.contrib import admin
from django.urls import path

from crudparts.views import (
    CrudpartsListView,
    CrudpartsCreateView,
    CrudpartsUpdateView,
    CrudpartsDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CrudpartsListView.as_view(), name="crudparts_list"),
    path("Create", CrudpartsCreateView.as_view(), name="crudparts_form"),
    path("update/<str:pk>", CrudpartsUpdateView.as_view(), name="crudparts_update"),
    path("delete/<str:pk>", CrudpartsDeleteView.as_view(), name="crudparts_delete"),
]
