from django.shortcuts import render
# Create your views here.
def showform(request):
    handle=request.POST.get('handle')
    print(handle)
    return render(request,'form.html')
def input_handle(request):
    handle = request.POST.get('handle')
    handle.lower()

    return render(request, 'donate.html')