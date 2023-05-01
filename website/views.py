#from django.shortcuts import render
from django.shortcuts import render
import gradio as gr
import os
import requests
# import torch
# from transformers import AutoProcessor, WhisperForConditionalGeneration
#from datasets import load_dataset
# import librosa
import os
# import pandas as pd
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from myapp.models import WhisperModel
from django.http import HttpResponse

API_URL = "https://api-inference.huggingface.co/models/basilkr/Whisper_Malasar_50"
headers = {"Authorization": "Bearer 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"}

def home(request):
    return render(request, 'ho.html',{})
def gradio_app(request):
    return render(request, 'gradio_app.html')

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def predict(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file'].file.read()

        try:
            output = query(audio_file)
            return JsonResponse(output, safe=False)
        except UnicodeDecodeError:
            return HttpResponse("Error: Invalid audio file", status=400)
    return render(request, 'predict.html')