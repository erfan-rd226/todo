from django.urls import path
from . import views

urlpatterns = [

#region for fungtoin view...

    # path('',views.all_todos),
    # path('<int:todo_id>',views.todo_detail_view),
    
#endregion


#region start class view...

    # path('',views.TodoListApiView.as_view()),
    # path('<int:todo_id>/',views.TodoDetailApaView.as_view()),

#endregion


    path('',views.TodoListMixinApiVeiw.as_view()),    


]
