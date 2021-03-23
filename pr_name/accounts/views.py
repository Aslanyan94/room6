from django.shortcuts import render
from django.http import HttpResponse


def accounts(request):
    # return HttpResponse("hello")
    return render(request, "accounts.html", context={"name": "Basic"})