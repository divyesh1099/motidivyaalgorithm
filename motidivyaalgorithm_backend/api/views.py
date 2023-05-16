from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
# Create your views here.

@api_view(["GET"])
def getMessage(request):
    current_user = request.user.pk
    messages = Message.objects.filter(user=current_user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postMessage(request):
    current_user = request.user.pk
    request.data["user"] = current_user
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)