class CountryResponse:
    __api = ""

    __country = ""
    __server = ""

    def __init__(self, api, server, country):
        self.__api = api
        self.__country = country
        self.__server = server

    def getCountry(self):
        return self.__api.getResponse(self.__getSpecificEndpoint()).json()

    def __getSpecificEndpoint(self):
        return f"{self.__api.getEndpoint('Country')}{self.__server}/{self.__country}"
