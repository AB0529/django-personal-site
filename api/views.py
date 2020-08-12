from django.shortcuts import render

def docs(req):
    return render(req, 'docs.html')