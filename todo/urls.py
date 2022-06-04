
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    # path('detail/<int:todo_pk>', views.eachDetail, name='each_detail'),
    path('todo/<int:pk>/update/', views.todoUpdate.as_view(), name='todo-detail'),
    path('complete/<int:todo_pk>', views.completeTodo, name='complete'),
    path("todo/update/<int:todo_pk>", views.updateTodo, name='update-todo'),
    path('deletecompleted', views.deleteCompleted, name='delete-completed'),
]
