class BaseContex:
    __title: str
    __subtitle: str
    __description: str
    __key: str

    def __init__(self, key: str, title: str):
        self.__key = key
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def subtitle(self):
        return self.__subtitle

    @subtitle.setter
    def subtitle(self, value):
        self.__subtitle = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
