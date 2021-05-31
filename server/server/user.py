import sys
import os

import pymysql.cursors
from userinfo import UserInfo
from dbutils import getDbConnection

class User:
    def __init__(self, username, password=""):
        self._username = username
        self._password = password

    def getUploadIds(self):
        with getDbConnection() as connection:
            with connection.cursor() as cursor:
                try:
                    uploadIds = []

                    fetchUploadIdsQuery = "select uploadid as uploadid from usernamexuploadidtbl WHERE username=%s"
                    cursor.execute(fetchUploadIdsQuery, (self._username,))

                    return [record["uploadid"] for record in cursor.fetchall()]

                except Exception as e:

                    return []

    def getUserInfo(self):
        return UserInfo.getUserInfo(username, password)

    def addUpload(uploadData):
        with getDbConnection(autocommit=False) as connection:
            with connection.cursor() as cursor:
                try:
                    nextUploadId = self.getNextUploadId()

                    uploadInsertQuery = "insert into uploadstbl values (%s)"
                    cursor.execute(uploadInsertQuery, (self._username,))

                    result = cursor.fetchone()

                    useridxupoadidtblInsertQuery = "insert into useridxupoadidtbl values (%d, %d)"

                    cursor.execute(useridxupoadidtblInsertQuery, (0, nextUploadId))

                    connection.commit()	

                    return True

                except Exception as e:
                    connection.rollback()

                    return False

    def getNextUploadId(self):
        nextUploadIdQuery = "SELECT AUTO_INCREMENT as auto_increment FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'usercredentialsdb' AND TABLE_NAME = 'uploadstbl'"
        with getDbConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(nextUploadIdQuery)
                result = cursor.fetchone()

                return result.get("auto_increment", None)
