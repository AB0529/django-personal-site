from github import Github
from django.shortcuts import render
from django.conf import settings
from datetime import datetime


def build_project_html(language, title, desc, link):
    """ Builds project card html with specified details """
    # Handle None language
    if not language:
        language = "atom"

    return {
        'lang': language.lower(),
        'title': title,
        'desc': desc,
        'link': link,
    }


def home(req):
    """ The home page of the site """
    g = Github(settings.GH_TOKEN)

    context = {}
    # Send projects
    context['projects'] = [build_project_html(
        repo.language, repo.name, 'No description' if not repo.description else repo.description, f'https://github.com/{repo.full_name}'
    ) for repo in g.get_user().get_repos()]
    context['current_year'] = datetime.now().year

    return render(req, 'home.html', context)
