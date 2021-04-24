from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

from json import dumps

from server.dbutils import tryLogin

def login(request, username, password):
   print("username: ", username)
   print("password: ", password)

   return tryLogin(request, username, password)

def splashpage(request):
   loginPgData = open("server/templates/login.html").read()
   response = HttpResponse(loginPgData)
   response["X-Content-Type-Options"] = "nosniff"
   response['Content-Length'] = len(loginPgData)
   response["Content-Type"] = "text/html"
   return render(request, "login.html", {})

@csrf_exempt
def addUserUpload(request):
    ##return render(request, "upload.html", {})
    return HttpResponse(dumps({"successful": True}))
