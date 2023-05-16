from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
from rest_framework import status
# Create your views here.

@api_view(["GET"])
def getAllUserMessages(request):
    current_user_id = request.user.pk
    messages = Message.objects.filter(user=current_user_id)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getMessageById(request, id=None):
    try:
        current_user_id = request.user.pk
        messageFromDb = Message.objects.get(id = id, user = current_user_id)
        serializer = MessageSerializer(messageFromDb)
        return Response(serializer.data)
    except Message.DoesNotExist:
        return status.HTTP_400_BAD_REQUEST

@api_view(["POST"])
def postMessage(request):
    current_user_id = request.user.pk
    request.data["user"] = current_user_id
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteMessage(request, id=None):
    try:
        messageToDelete = Message.objects.get(id = id)
        messageToDelete.delete()
        return status.HTTP_200_OK
    except Message.DoesNotExist:
        return status.HTTP_400_BAD_REQUEST
