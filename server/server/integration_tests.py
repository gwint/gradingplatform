import dbutils

def test_getDbConnection():
    assert dbutils.getDbConnection()

def test_getEmptyUserData():
    assert dbutils.getEmptyUserData() == {} 

def test_getUserInfo():

    assert True

def test_addUserUpload():
    assert True

def test_areUserCredentialsValid_present():
    testUsername = "username"
    testPassword = "password"

    assert dbutils.areUserCredentialsValid(testUsername, testPassword)

def test_areUserCredentialsValid_missing():
    testUsername = "notpresent"
    testPassword = "notpresent"

    assert not dbutils.areUserCredentialsValid(testUsername, testPassword)


if __name__ == "__main__":
    print("Running tests for db accessor code")
