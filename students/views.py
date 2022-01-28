from django.shortcuts import render

# Create your views here.

def studentlist(request):
    return render(request, 'studentlist.html')
