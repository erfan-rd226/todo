from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',views.TodoViewSetApiView)


urlpatterns = [

#region for fungtoin view...

    # path('',views.all_todos),
    # path('<int:todo_id>',views.todo_detail_view),
    
#endregion


#region start class view...

    # path('',views.TodoListApiView.as_view()),
    # path('<int:todo_id>/',views.TodoDetailApaView.as_view()),

#endregion


#region mixin...

    # path('',views.TodoListMixinApiVeiw.as_view()),
    # path('<pk>/',views.TodoDetaiMixinApiVeiw.as_view()),    

#endregion


#region generics

    # path('',views.TodoListGenericApiVeiw.as_view()),
    # path('<pk>/',views.TodoDetailGenericApiVeiw.as_view()),

#endregion


#region viewset

path('',include(router.urls))


#endregion

]
