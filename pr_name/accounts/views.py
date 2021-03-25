from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def accounts(request):
    # username = request.body["username"]
    # password = request.body["password"]
    # # User.objects.create_user(username=username, password=password)

    # user = User()
    # user.username = username
    # user.password = password
    # user.save(commit=True)
    # return HttpResponse("hello")
    return render(request, "accounts.html", context={"name": "Basic"})