import os

from django.shortcuts import render


def index(request):
    context = {
        "key": os.environ["API_KEY"],
        "sec": os.environ["API_SEC"]
    }
    return render(request, 'app/base.html', context)
