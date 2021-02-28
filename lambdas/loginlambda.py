import json

import mysql.connector
import sys
import boto3
import os
import pymysql.cursors


ENDPOINT="usercredentialsdb.c3fbnwkqmhbb.us-east-1.rds.amazonaws.com"
PORT="3306"
USR="gwint"
REGION="us-east-1d"
DBNAME="usercredentialsdb"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
     
                
def lambda_handler(event, context):
    connection = pymysql.connect(host='usercredentialsdb.c3fbnwkqmhbb.us-east-1.rds.amazonaws.com',
                             user='admin',
                             password='password',
                             database='usercredentialsdb',
                             cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            print(event)
            sql = "select username from logincredentialstbl where username=%s"
            cursor.execute(sql, (event["username"],))
            
            result = cursor.fetchone()
            print(result)
            
            if result:
                return {"addedSuccessful": False}
            else:
                
                sql = "insert into `logincredentialstbl` values (%s, %s)"
                cursor.execute(sql, (event["username"], event["password"]))
                connection.commit()
                return {"addedSuccessful": True}
                
    item_count = 0
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!') + '\n'
    }


