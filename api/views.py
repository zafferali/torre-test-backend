from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def getUser(request):
    getUserUrl = "https://torre.bio/api/bios/zafferali" 
    response = requests.get(getUserUrl)
    data = response.json()
    print(data)
    return Response(data)
