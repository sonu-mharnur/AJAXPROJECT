from django.shortcuts import render
from django . http import HttpResponse, HttpResponseRedirect
from.forms import uploadFileForm
from .models import FileData
# Create your views here.
def upload_file(request):
    if request. method == 'post':
        form = uploadFileForm(request.post.request.FILSE)
        if form.is_valid():
            instance= FileData(title=request.POST['title'],filename=request.FILES['filename'])
            instance.save()
            return HttpResponseRedirect('/uploadfile/')
    else:
        form = uploadFileForm()

    return render(request,'uploadfile.html',{'form':form})