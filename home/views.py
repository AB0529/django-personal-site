from django.shortcuts import render


def home(req):
    """ The home page of the site """
    return render(req, 'home.html')
