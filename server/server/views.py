from django.http import HttpResponse
from django.shortcuts import render


def login(request, username, password):
   text = """<h1>welcome to my app good sir!</h1>"""
   #return HttpResponse(text)
   return render(request, "hello.html", {})

def splashpage(request):
   loginPgData = open("server/templates/login.html").read()
   response = HttpResponse(loginPgData)
   response["X-Content-Type-Options"] = "nosniff"
   response['Content-Length'] = len(loginPgData)
   response["Content-Type"] = "text/html"
   #return response 
   return render(request, "login.html", {})
