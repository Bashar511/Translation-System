from django.shortcuts import render ,get_object_or_404,redirect
from .api import hel_en2ar
from .forms import *
from .subtitle_parser import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import (UpdateView)
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.base import ContentFile
from django.urls import reverse

def instant(request):
    if request.method == 'POST':
        text = request.POST['text_field']
        processed_text = hel_en2ar(text)
        context = {
        'unprocessed' : text,
        'processed' : processed_text,
        }
    else:
        context = {
            'unprocessed' : '',
            'processed' : '',
        }
    return render(request, "instant_translation.html", context)


@login_required
def browse(request):
    owned_projects = Project.objects.filter(owner=request.user)
    member_projects = Project.objects.filter(
        projectmember__granted_to=request.user
    )
    all_projects = (owned_projects | member_projects).distinct()
    return render(request, 'browse_projects.html', {'form_out': all_projects})


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
            return redirect(reverse('translation:browse'))
        else:
            return render(request,'create_project.html',{'form':form})
    form=projectForm()
    return render(request,'create_project.html',{'form':form})


class PostUpdateView(UpdateView):
    model = Project
    fields = ('title','fileEN','deliverytime',)
    template_name = 'current.html'
    context_object_name = 'updateform'
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        updateform=form.save(commit=False)
        updateform.updated_dt = timezone.now()
        updateform.save()
        return redirect(reverse('translation:browse'))



def details(request,x):
    project = get_object_or_404(Project,pk=x)
    title=project.title
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
       
        number = request.POST.get('number', 1)  
        decision = request.POST.get('final_decision', '') 

        context = {
            'title':title,
            'fileEN' : processed_fileEN,
            'fileAR' : processed_fileAR_after,
            'decision':decision,
            'ID':number,
            
        }
        processed_fileAR_after[int(number)]["sentence"]=decision
        create_srt(processed_fileAR_after, fileAR.path)
    else:
        context = {
            'title':title,
            'fileEN' : processed_fileEN,
            'fileAR' : processed_fileAR_after,
            'decision':'',
            'ID':1,
        }
    return render(request, "details.html", context)




def delete(request,x):
    project = get_object_or_404(Project, id=x)
    project.delete()
    return redirect('translation:browse')  



def grant_permission(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST,user=request.user)
        if form.is_valid():
                permission = form.save(commit=False)
                if permission.project.owner == request.user:
                    permission.save()
                    return redirect('translation:browse') 
    else:
        form = PermissionForm(user=request.user)

    return render(request, 'grant_permission.html', {'form': form})




def CONTACTUS(request):
    return render(request,'contact.html')



def ABOUTUS(request):
    return render(request,'about.html')