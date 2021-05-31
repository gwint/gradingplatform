import sys
import os
import pymysql.cursors
from django.shortcuts import render
from server.dbutils import getDbConnection, areUserCredentialsValid


def tryLogin(request, username, password):
    if areUserCredentialsValid(username, password):
        return render(request, "upload.html", {"username": username})
    else:
        return render(request, "login.html", {})

def getEmptyUserData():
    return {}
