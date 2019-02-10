import logging
import os

from django.shortcuts import redirect
from django.shortcuts import render


def index(request):

    # full_url = request.build_absolute_uri()
    # if "shekels" in full_url:
    #     if "http://" in full_url:
    #         full_url = full_url.replace("http", "https")
    #         return redirect(full_url)

    context = {
        "key": os.environ["API_KEY"],
        "sec": os.environ["API_SEC"]
    }
    return render(request, 'app/base.html', context)
