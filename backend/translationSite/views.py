from django.shortcuts import render ,get_object_or_404,redirect
from django.http import HttpResponse
from .api import hel_en2ar, bart_en2ar
from .forms import *
from .subtitle_parser import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import (UpdateView)
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.base import ContentFile

def instant(request):
    if request.method == 'POST':
        text = request.POST['text_field']
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
    return render(request, "instant_translation.html", context)

@login_required
def browse(request):
    allproject=project1.objects.filter(owner=request.user)
    return render(request,'browse_projects.html',{'form_out':allproject})


def create (request):
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        title = request.POST.get('title')
        if form.is_valid() :
            form_instance = form.save(commit=False)
            form_instance.owner=request.user
            srt_content = "1\n00:00:00,000 --> 00:00:05,000\n"  
            file_name = f"{title}.srt"
            form_instance.fileAR.save(file_name, ContentFile(srt_content))
            form_instance.save()
        else:
            return render(request,'create_project.html',{'form':form})
    form=projectForm()
    return render(request,'create_project.html',{'form':form})


class PostUpdateView(UpdateView):
    model = project1
    fields = ('title','fileEN','deliverytime',)
    template_name = 'current.html'
    context_object_name = 'updateform'
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        updateform=form.save(commit=False)
        updateform.updated_dt = timezone.now()
        updateform.save()
        return redirect('browse_projects.html')



def test(request,x):
    project = get_object_or_404(project1,pk=x)
    fileEN=project.fileEN
    fileAR=project.fileAR
    processed_fileEN =parse_srt(fileEN.path) 
    processed_fileAR_before =parse_srt(fileAR.path) 
    processed_fileAR_after={}
    
    #to be fixed
    for key, value in processed_fileEN.items():
            processed_fileAR_after[key]= {
            "ID": key,
            "start_time":value["start_time"],
            "end_time":value["end_time"],
            "sentence":'',
            }
    for key, value in processed_fileAR_before.items():
        processed_fileAR_after[key]["sentence"]=processed_fileAR_before[key]["sentence"]
    if request.method == 'POST':
        try:
            number=request.POST['number']
        except MultiValueDictKeyError:
            number=1
            
        try:
            decision=request.POST['final_decision']
        except MultiValueDictKeyError:
            decision=''
            
        try:
            text = request.POST['text_field']
        except MultiValueDictKeyError:
            text = ''
        processed_text = bart_en2ar(text)
        context = {
            'unprocessed' : text,
            'processed' : processed_text,
            'fileEN' : processed_fileEN,
            'fileAR' : processed_fileAR_after,
            'decision':decision,
            'ID':number,
        }
        processed_fileAR_after[int(number)]["sentence"]=decision
        create_srt(processed_fileAR_after, fileAR.path)
    else:
        context = {
            'unprocessed' : '',
            'processed' : '',
            'fileEN' : processed_fileEN,
            'fileAR' : processed_fileAR_after,
            'decision':'',
            'ID':1,
        }
    return render(request, "test.html", context)



