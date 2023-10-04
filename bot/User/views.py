from django.shortcuts import render
from django.http import HttpResponse
from User.forms import ContastantRegstration
from User.models import Contastant,Handle_Name
# Create your views here.
def Profile(request):
    return HttpResponse('<h1>This is the Profile Section</h1>')

def contastant_info(request):
    con = Contastant.objects.all()
    return render(request,'show.html',{'cont': con})

def showform(request):
    fm = ContastantRegstration()
    handle=request.POST.get('handle')
    if handle!=None:
        ob=Handle_Name(
            Name=handle
        )
        ob.save()
    return render(request,'form.html',{'form':fm})

def show_handle(request):
    data=Handle_Name.objects.all()
    dic=[]
    for i in data:
        dic.append(i.Name)

    return render(request,'show_handle.html',{'data':dic})

