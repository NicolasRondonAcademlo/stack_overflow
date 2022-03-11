from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def user_create(request):

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(
           users, many=True
        )
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors, status=400)