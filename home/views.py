from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest , JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response

def index_paje(request):
    context = {'todos' : Todo.objects.order_by('priority').all()
    }           
    return render(request,'home/index.html',context)

def todos_lsan(request = Request):
    todos = list(Todo.objects.order_by('priority').all().values('title','is_done'))
    return Response({'todos':todos})