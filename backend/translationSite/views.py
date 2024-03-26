from django.shortcuts import render ,get_object_or_404,redirect
from django.http import HttpResponse
from .api import hel_en2ar, bart_en2ar
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import (UpdateView)


def instant(request):
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
    return render(request, "instant_translation.html", context)


@login_required
def browse(request):
    allproject=project1.objects.filter(author=request.user)
    # allproject=""
    return render(request,'browse_projects.html',{'form_out':allproject})



def create (request):
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid() :
            form = form.save(commit=False)
            form.author=request.user
            form.save()
        else:
            return render(request,'create_project.html',{'form':form})
    form=projectForm()
    return render(request,'create_project.html',{'form':form})
    
    

# def current (request,id):
#     details = get_object_or_404(project1,id=id)
#     # details_AI = get_object_or_404(output_AI,title_id=id)
#     print(details)
#     return render(request,'current.html',{'details':details})


class PostUpdateView(UpdateView):
    model = project1
    # fields = ('title','publish','deliverytime','fileEN')
    fields = ('title','fileEN','deliverytime',)
    template_name = 'current.html'
    context_object_name = 'updateform'
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        updateform=form.save(commit=False)
        print("11111111")

        updateform.updated_dt = timezone.now()
        
        updateform.save()
        return redirect('project')


