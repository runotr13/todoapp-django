from django.urls import path
from .views import TodoCreate,TodoUpdate,TodoDelete
urlpatterns = [
    path('',TodoCreate,name="todocreate"),
    path('todoUpdate/<int:id>',TodoUpdate,name="todoupdate"),
    path('todoDelete/<int:id>',TodoDelete,name="tododelete"),
]