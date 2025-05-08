from django.shortcuts import render,HttpResponse



def master(request):
    return render(request, 'master.html')


def index(request):
    return render(request,'index.html')

# def master(request):
#     return ('HELLO ')
