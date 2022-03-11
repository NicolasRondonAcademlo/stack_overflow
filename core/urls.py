from django.urls import  path, include
from .views import user_create

urlpatterns = [
    path("questions/",include( "api_app.urls")),
    path("user/", user_create)
]