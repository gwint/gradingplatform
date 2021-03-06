import dbutils
import siteutils
import userinfo
import user

def test_getDbConnection():
    assert dbutils.getDbConnection()

def test_getEmptyUserData():
    assert siteutils.getEmptyUserData() == {} 

def test_areUserCredentialsValid_present():
    testUsername = "username"
    testPassword = "password"

    assert dbutils.areUserCredentialsValid(testUsername, testPassword)

def test_areUserCredentialsValid_missing():
    testUsername = "notpresent"
    testPassword = "notpresent"

    assert not dbutils.areUserCredentialsValid(testUsername, testPassword)

def test_UserInfo_getters():
    testUserInfo = userinfo.UserInfo("firstname", "lastname", "username", "password")
    assert testUserInfo.getFirstname() == "firstname"
    assert testUserInfo.getLastname() == "lastname"
    assert testUserInfo.getUsername() == "username"
    assert testUserInfo.getPassword() == "password"

def test_UserInfo_getUserInfo():
    for testUserInfo in [userinfo.UserInfo.getUserInfo("username", "password"), \
            userinfo.UserInfo.getUserInfo("username")]:

        assert testUserInfo.getFirstname() == "firstname"
        assert testUserInfo.getLastname() == "lastname"
        assert testUserInfo.getUsername() == "username"
        assert testUserInfo.getPassword() == "password"

def test_User_getNextUploadId():
    testUser = user.User("username", "password")
    nextUploadId = testUser.getNextUploadId()
    assert nextUploadId > 0

def test_User_getUploadsInfo():
    testUser = user.User("username", "password")
    uploadIds = testUser.getUploadsInfo()
    assert uploadIds == [{"uploadid": 1, "uploadname":"testupload2"}, \
                         {"uploadid": 2, "uploadname":"testupload2"}, \
                         {"uploadid": 3, "uploadname":"testupload2"}, \
                         {"uploadid": 4, "uploadname":"testupload2"}, \
                         {"uploadid": 5, "uploadname":"testupload2"}]


'''
def test_User_addUpload():
    testUser = user.User("username", "password")
    assert testUser.addUpload("testupload2", b"123abc")
'''

if __name__ == "__main__":
    print("Running tests for db accessor code")
