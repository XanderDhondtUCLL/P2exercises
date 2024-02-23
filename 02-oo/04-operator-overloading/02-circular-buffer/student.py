class CircularBuffer:
    def __init__(self, max_n:int) -> None:
        self.__max_n = max_n
        self.__items = []

    def add(self, value):
        self.__items.append(value)
        if len(self.__items) > self.__max_n:
            del self.__items[0]

    def __len__(self):
        return self.__max_n
    
    def __getitem__(self, index):
        return self.__items[index]
    

buffer = CircularBuffer(5)

buffer.add('a')
buffer.add('b')
buffer.add('c')
buffer.add('d')
buffer.add('e')
buffer.add('f')

print(buffer[0])