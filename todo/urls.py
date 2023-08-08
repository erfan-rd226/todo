from django.urls import path
from . import views

urlpatterns = [
    #for fungtoin view...
    # path('',views.all_todos),
    # path('<int:todo_id>',views.todo_detail_view),
    
    #start class view...
    path('',views.TodoListApiview.as_view()),
]
