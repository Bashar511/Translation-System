from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .api import hel_en2ar, bart_en2ar

def home(request):
    if request.method == 'POST':
        text = request.POST['text_field']
        #processed_text = hel_en2ar(text)
        processed_text = bart_en2ar(text)
        context = {
        'unprocessed' : text,
        'processed' : processed_text,
        
         }
    else:
        context = {
            'unprocessed' : '',
            'processed' : 'Translated Text',
           
        }
    return render(request, "../templates\index.html", context)