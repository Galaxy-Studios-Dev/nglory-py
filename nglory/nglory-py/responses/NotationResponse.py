class NotationResponse:
    __api = ""

    __week = "2842"
    __country = ""
    __server = ""

    def __init__(self, api, server, country, week):
        self.__api = api

        self.__server = server
        self.__country = country
        self.__week = week

    def getNotation(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint('Notations')}week={self.__week}&country={self.__country}&server={self.__server}"
