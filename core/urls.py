from django.urls import  path, include
from .views import user_create, user_get_info

urlpatterns = [
    path("questions/",include( "api_app.urls")),
    path("user/", user_create),
    path("user/<int:pk>/", user_get_info)
]