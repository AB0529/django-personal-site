from github import Github
from django.shortcuts import render
from django.conf import settings


def build_project_html(language, title, desc, link):
    """ Builds project card html with specified details """
    # Handle None language
    if not language:
        language = "atom"

    return f'<div class="col s12 m6"> <div class="card blue-grey darken-2"> <div class="card-content white-text"> <span class="card-title"> <i class="devicon-{language.lower()}-plain colored"></i> | <strong>{title}</strong></span> <p>{desc}</p></div><div class="card-action"> <a href="{link}" target="_blank" class="blue-grey darken-4 btn"> <i class="devicon-github-plain colored"></i> <strong>Source</strong></a> </div></div></div>'


def home(req):
    """ The home page of the site """
    g = Github(settings.GH_TOKEN)
    # Build all projects into html string
    projects_html = [build_project_html(
        repo.language, repo.name, 'No description' if not repo.description else repo.description, repo.url
    ) for repo in g.get_user().get_repos()]

    # Send projects html
    context = {}
    context['projects'] = projects_html

    return render(req, 'home.html', context)
