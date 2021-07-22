from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

from json import dumps, loads

from server.siteutils import tryLogin, addUpload, getUploads


## TODO: Delete as loginNoArgs should be used instead
'''
def login(request, username, password):
    print(str(request))
    print(request.content_type)
    print(f"RequestDump = {request.POST}")
    return tryLogin(request, username, password)
'''

def loginNoArgs(request):
    print("Inside loginNoArgs")
    print(f"RequestDump = {request.body}")
    print(str(request))
    print(request.content_type)
    print(request.POST["username"])
    print(request.POST["password"])
    print(f"RequestDump = {request.POST}")
    username = request.POST["username"]
    password = request.POST["password"]

    return tryLogin(request, username, password)


def splashpage(request):
   loginPgData = open("server/templates/login.html").read()
   response = HttpResponse(loginPgData)
   response["X-Content-Type-Options"] = "nosniff"
   response['Content-Length'] = len(loginPgData)
   response["Content-Type"] = "text/html"
   return render(request, "login.html", {})

## TODO: Add code to retrieve user uploads from db
def getUserUploads(request):
    requestDict = loads(request.body)
    username = requestDict["username"]

    uploads = getUploads(username)
    print("uploads:", uploads)
    if len(uploads) == 0:
        console.log("No uploads retrieved for this user")

    return HttpResponse( \
                dumps(\
                    { \
                        "uploads": uploads \
                    } \
                ) \
           )
    return 

@csrf_exempt
def addUserUpload(request):
    requestDict = loads(request.body)
    fileName = requestDict["selectedFile"]
    fileData = requestDict["fileData"]
    username = requestDict["username"]

    isAddSuccessfull = addUpload(fileName, fileData, username)
    uploads = []
    if isAddSuccessfull:
        uploads = getUploads(username) 
        print("uploads:", uploads)

    return HttpResponse( \
                dumps(\
                    { \
                        "successful": isAddSuccessfull, \
                        "uploads": uploads \
                    } \
                ) \
           )
