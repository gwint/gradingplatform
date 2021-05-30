from server.dbutils import getDbConnection

class UserInfo:
    def __init__(self, firstname, lastname, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self._username = username
        self._password = password

    def getFirstname(self):
        return self._firstname

    def getLastname(self):
        return self._lastname

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password

    @staticmethod
    def getUserInfo(username, password=""):
        with getDbConnection() as connection:
            with connection.cursor() as cursor:
                sql = "select firstname as firstname, lastname as lastname, username as username, password as password from userinfotbl where username=%s"
                if password:
                    sql += ' '  + "AND password=%s"

                cursor.execute(sql, (username, password) if password else (username,))

                userInfo = None
                result = cursor.fetchone()
                if result:
                    userInfo = UserInfo(result["firstname"], \
                                        result["lastname"],  \
                                        result["username"],  \
                                        result["password"])

                return userInfo
