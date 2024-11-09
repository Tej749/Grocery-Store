from django.urls import path
from . import views
from .views import edit_form

urlpatterns = [
    path("", views.inventory, name="inventory"),
    path("form", views.form, name="form"),
    path("form/edit/<pk>", views.edit_form, name="edit"),
    path("form/delete/<pk>", views.delete_form, name="delete"),


]
