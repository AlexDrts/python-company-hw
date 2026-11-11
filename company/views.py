from django.shortcuts import render


def home(request, **kwargs):
    return render(request, 'home.html', {'active': 'home'})


def news(request, **kwargs):
    return render(request, 'news.html', {'active': 'news'})


def management(request, **kwargs):
    return render(request, 'management.html', {'active': 'management'})


def about(request, **kwargs):
    return render(request, 'about.html', {'active': 'about'})


def contacts(request, **kwargs):
    return render(request, 'contacts.html', {'active': 'contacts'})
