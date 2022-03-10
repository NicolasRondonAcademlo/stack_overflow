from django.urls import  path
from .views import question_list

urlpatterns = [
    path("api/questions/", question_list),
]