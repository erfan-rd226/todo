from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializers
from .models import Todo

@api_view(['GET','POST'])
def all_todos(request:Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializers(todos , many=True)
        return Response(todo_serializer.data , status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(None,status.HTTP_400_BAD_REQUEST)