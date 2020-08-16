from django.shortcuts import render
from django.conf import settings
from requests import get
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_screenshots():
	''' Will get all screenshots in database from API '''
	req = get(f'https://api.anishb.net/screenshots/all/{settings.API_KEY}')

	return req.json()["result"]

@login_required
def home(req):
	get_screenshots()
	context = {}
	context["screenshots"] = [{
		"name": ss["name"],
		"img": ss["image"]["Data"],
		"date": ss["timestamp"]
	} for ss in get_screenshots()]


	return render(req, "pics/pics.html", context)