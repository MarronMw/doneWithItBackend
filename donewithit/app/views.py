from django.shortcuts import render

# Create your views here.
def trial(request):
    return render(request,"index.html")
