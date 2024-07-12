
class NGIslandResponse:
    __api = ""
    __page = ""

    def __init__(self, api, page):
        self.__api = api
        self.__page = page

    def getPage(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint("NGIslands")}?page={self.__page}"