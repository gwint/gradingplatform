import sys
import os

import pymysql.cursors
from server.userinfo import UserInfo
from server.dbutils import getDbConnection

class User:
    def __init__(self, username, password=""):
        self._username = username
        self._password = password

    def getUploadsInfo(self):
        with getDbConnection() as connection:
            with connection.cursor() as cursor:
                try:
                    uploadIds = []

                    fetchUploadsInfoQuery = 'select b.uploadid as uploadid, b.uploadname as uploadname from usernamexuploadidtbl as a inner join uploadstbl as b on a.uploadid=b.uploadid where a.username=%s'
                    cursor.execute(fetchUploadsInfoQuery, (self._username,))

                    return [x for x in cursor.fetchall()]

                except Exception as e:
                    print(e)
                    raise e

                    return []

    def getUserInfo(self):
        return UserInfo.getUserInfo(username, password)

    def addUpload(self, uploadName, uploadData):
        with getDbConnection() as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                try:
                    nextUploadId = self.getNextUploadId()

                    uploadInsertQuery = "insert into uploadstbl (uploadname, data) values (%s, %s)"
                    cursor.execute(uploadInsertQuery, (uploadName, uploadData))

                    usernamexuploadidtblInsertQuery = "insert into usernamexuploadidtbl (username, uploadid) values (%s, %s)"

                    cursor.execute(usernamexuploadidtblInsertQuery, (self._username, nextUploadId))

                    connection.commit()	

                    return True

                except Exception as e:
                    connection.rollback()
                    raise e

                    return False

    def getNextUploadId(self):
        nextUploadIdQuery = "SELECT count(*) as next_id from uploadstbl"
        with getDbConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(nextUploadIdQuery)
                result = cursor.fetchone()

                nextId = result.get("next_id", None)
                return nextId + 1

