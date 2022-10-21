from django.shortcuts import redirect, render
from redis import Redis

from .models import Item

redis = Redis(host="redis", port=6379)


def home(request):

    return render(request, "home.html")
