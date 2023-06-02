from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework import status 

@api_view(['GET'])
def getUserSkills(request, username):
    url = f"https://torre.bio/api/bios/{username}" 
    response = requests.get(url)

    if response.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if response.status_code == 200:
        person = response.json()['person']
        skills = response.json()['strengths']
        user = {
            "name": person['name'],
            "picture": person['picture'],
            "skills": skills,
        } 
        return Response(user)
