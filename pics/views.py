import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


def get_screenshots():
	''' Will get all screenshots in database from API '''
	r = requests.get(f'{settings.API_HOST}/all/{settings.API_KEY}')

	return r.json()["result"]


@login_required
def delete_screenshot(req):
	name = req.GET.get('name')
	r = requests.delete(f'{settings.API_HOST}/{settings.API_KEY}/{name}')
	r = r.json()

	if r["state"] == "fail":
		return HttpResponse()

	return HttpResponse()

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
