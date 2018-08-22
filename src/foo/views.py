from django.shortcuts import render
import json
from django.http import HttpResponse
from . import tasks


# Create your views here.
def index(request):
    print("fooooooobarrrrr")
    tasks.bar()
    return HttpResponse(
        json.dumps({
            "msg": "bar"
        }), content_type='application/json')
