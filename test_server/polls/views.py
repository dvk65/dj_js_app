from rest_framework import generics

from .models import Todo
from .serial import TodoSerializer

from django.shortcuts import render
from django.http import HttpResponse

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
def index(request):
    return HttpResponse("Hello, world. We got polls!")


# Create your views here.
