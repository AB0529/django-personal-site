import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def get_screenshots():
	''' Will get all screenshots in database from API '''
	r = requests.get(f'https://api.anishb.net/screenshots/all/{settings.API_KEY}')

	return r.json()["result"]

@login_required
def delete_screenshot(req, name):
	r = requests.delete(f'https://api.anishb.net/screenshots/{settings.API_KEY}/{name}')
	r = r.json()

	if r["state"] == "fail":
		return HttpResponseRedirect('/')

	return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

@login_required
def home(req):
	get_screenshots()
	context = {}
	context["delete_url"] = f'{settings.API_HOST}/screenshots/{settings.API_KEY}'
	context["screenshots"] = [{
		"name": ss["name"],
		"img": ss["image"]["Data"],
		"date": ss["timestamp"]
	} for ss in get_screenshots()]


	return render(req, "pics/pics.html", context)
