from django.urls import path

from task import views

urlpatterns = [
    path('', view=views.index, name='index'),
]