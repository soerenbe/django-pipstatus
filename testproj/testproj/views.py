from django.shortcuts import render


def pipconfig(request):
    return render(request, "mypip.html")


def pipconfig2(request):
    return render(request, "mypip2.html")