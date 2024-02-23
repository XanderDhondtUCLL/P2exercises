class LengthConverter:
    def __init__(self) -> None:
        self.__meter = 0
        self.__feet = 0
        self.__inch = 0


    def clear_values(self):
        self.__meter = 0
        self.__feet = 0
        self.__inch = 0

    @property
    def meter(self):
        return self.__meter
    
    @property
    def feet(self):
        return self.__feet
    
    @property
    def inch(self):
        return self.__inch
    
    @meter.setter
    def meter(self, value):
        self.clear_values()
        self.__meter = value
        self.__feet = self.__meter * 3.28
        self.__inch = self.__feet * 12
    
    @feet.setter
    def feet(self, value):
        self.clear_values()
        self.__feet = value
        self.__inch = self.__feet * 12
        self.__meter = self.__feet / 3.28

    @inch.setter
    def inch(self, value):
        self.clear_values()
        self.__inch = value
        self.__feet = self.__inch / 12
        self.__meter = self.__feet / 3.28


