class UserResponse:
    __api = ""

    __username = ""

    def __init__(self, api, username):
        self.__api = api
        self.__username = username

    def getUser(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint('User')}{self.__username}"
