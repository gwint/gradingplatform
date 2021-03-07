import json

import mysql.connector
import sys
import boto3
import os
import pymysql.cursors
from django.shortcuts import render


DB_ENDPOINT="usercredentialsdb.c3fbnwkqmhbb.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
PASSWORD="password"
REGION="us-east-1d"
DBNAME="usercredentialsdb"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'


def getDbConnection():
    return pymysql.connect(host=DB_ENDPOINT,
                           user=USER,
                           password=PASSWORD,
                           database=DBNAME,
                           cursorclass=pymysql.cursors.DictCursor)

                
def tryLogin(request, username, password):
    with getDbConnection() as connection:
        with connection.cursor() as cursor:
            sql = "select username from logincredentialstbl where username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            
            result = cursor.fetchone()
            
            if not result:
                print("Login failed")
                return render(request, "login.html", {})
            else:
                print("Login succesful")
                #sql = "insert into `logincredentialstbl` values (%s, %s)"
                #cursor.execute(sql, (username, password))
                #connection.commit()
                return render(request, "upload.html", {"username": username})

def getEmptyUserData():
    return {}

def getUserInfo(username):
    with getDbConnection() as connection:
        with connection.cursor() as cursor:
            sql = "select username from userinfotbl where username=%s"
            cursor.execute(sql, (username,))
            
            result = cursor.fetchone()
            
            if result:
                return {"addedSuccessful": True, "userInfo": result}
            else:
                return {"addedSuccessful": False, "userInfo": result}


def addUserUpload(username, data):
    pass
