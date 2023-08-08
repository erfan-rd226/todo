from django.shortcuts import render, get_object_or_404

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


# added put and delete 

@api_view(['GET','PUT','DELETE'])
def todo_detail_view (requst:Request , todo_id:int):
    # try:
    #     todo=Todo.objects.get(pk=todo_id)
    # except Todo.DoesNotExist:
    #     return Response(None,status.HTTP_404_NOT_FOUND)
    
    todo = get_object_or_404(Todo, id=todo_id)
    
    if requst.method == 'GET':
        serializer = TodoSerializers (todo)
        return Response(serializer.data , status.HTTP_200_OK)
    
    elif requst.method == 'PUT':
        serializer = TodoSerializers (todo,data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif requst.method == 'DELETE':
        todo.delete()
        return Response(None , status.HTTP_204_NO_CONTENT)
