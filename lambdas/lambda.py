import json

import mysql.connector
import sys
import boto3
import os

ENDPOINT="usercredentialsdb.c3fbnwkqmhbb.us-east-1.rds.amazonaws.com"
PORT="3306"
USR="gwint"
REGION="us-east-1d"
DBNAME="usercredentialsdb"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

query_results = None
try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))          
                

def handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!') + '\n' ##+ query_results
    }

