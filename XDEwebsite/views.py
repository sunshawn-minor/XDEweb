from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
import sqlite3

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def indexpage(request):
    context = {}
    return render(request, 'index.html', context)

def dino_play(request):
    context = {}
    return render(request, 'dino-play.html', context)

def contact_us(request):
    context = {}
    return render(request, 'contact-us.html', context)

@api_view(['POST'])
def collect_info(request):
    info = JSONParser().parse(request)
    db = sqlite3.connect(os.path.join(BASE_DIR, 'db\student.sqlite3'))
    myCursor = db.cursor()
    myCursor.execute(
        'INSERT INTO INFO VALUES ("{0}", "{1}", "{2}");'.format(
        info['name'], 
        info['wechat-id'], 
        info['experience']
    ))
    db.commit()
    return JsonResponse({'message': 'loaded successfully!'}, status=status.HTTP_200_OK)