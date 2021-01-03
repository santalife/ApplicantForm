class eDoctor:
    def __init__(self,link="https://helloworld-hq.daily.co/helloworld2"):
        self.__link=link

    def set_link(self,link):
        self.__link=link

    def get_link(self):
        return self.__link


class patient:
    def __init__(self):
        self.__link=""

    def set_link(self,link):
        self.__link=link

    def get_link(self):
        return self.__link
