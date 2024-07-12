class MarketResponse:
    __api = ""

    __server = ""

    def __init__(self, api, server):
        self.__api = api
        self.__server = server

    def getMarket(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint('Market').replace('..', self.__server)}"
