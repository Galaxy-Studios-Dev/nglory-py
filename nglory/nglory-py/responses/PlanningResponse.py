class PlanningResponse:
    __api = ""
    __server = ""
    __month = ""
    __year = ""

    def __init__(self, api, server, month, year):
        self.__api = api
        self.__server = server
        self.__month = month
        self.__year = year

    def getPlanning(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint('Planning')}?server={self.__server}&month={self.__month}year={self.__year}"