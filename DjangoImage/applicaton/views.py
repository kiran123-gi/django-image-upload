from django.shortcuts import render,redirect
from.models import imageModel
from .forms import imageForms
def test_case(request):
    if request.method=="POST":
        form=imageForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("images")
    else:
        form = imageForms
    return render(request,"frontend/index.html",{"form":form,"form":form})
def image_list(request):
    objects=imageModel.objects.all()
    return render(request,"frontend/display.html",{"objects":objects})