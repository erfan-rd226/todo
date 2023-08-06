from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializers
from .models import Todo

@api_view(['GET'])
def all_todos(request:Request):
    todos = Todo.objects.order_by('priority').all()
    todo_serializer = TodoSerializers(todos , many=True)
    return Response(todo_serializer.data , status.HTTP_200_OK)