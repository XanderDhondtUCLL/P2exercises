class Duration:
    def __init__(self, time_in_seconds) -> None:
        self.__time_in_seconds = time_in_seconds

    @property
    def seconds(self):
        return self.__time_in_seconds
    
    @property
    def minutes(self):
        return self.__time_in_seconds / 60
    
    @property
    def hours(self):
        return self.minutes / 60
    
    @staticmethod
    def from_seconds(value):
        return Duration(value)
    
    @staticmethod
    def from_minutes(value):
        return Duration(value * 60)
    
    @staticmethod
    def from_hours(value):
        return Duration(value * 3600)