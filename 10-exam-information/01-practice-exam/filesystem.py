# Enter your code here:
from abc import ABC, abstractmethod
import re

class StorageDevice:
    def __init__(self, block_count: int, block_size: int) -> None:
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return (len(self.__available_blocks) + len(self.__used_block_count))
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count: int) -> list:
        if block_count > len(self.__available_blocks):
            raise RuntimeError()
        
        allocated_blocks = list(self.__available_blocks)[:block_count]
        for block in allocated_blocks:
            self.__available_blocks.remove(block)
            self.__used_blocks.add(block)

        return allocated_blocks
    
    def free(self, blocks: list) -> None:
        if not all(block in self.__used_blocks for block in blocks):
            raise RuntimeError()
        
        for block in blocks:
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)
        
class Entity(ABC):
    @staticmethod
    def is_valid_name(value):
        return re.fullmatch(r'[a-zA-z\d.]{1,16}', value)
    
    def __init__(self, storage: StorageDevice, name: str) -> None:
        if not self.is_valid_name(name):
            raise RuntimeError('Name is not valid!')
        self.__storage = storage
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise RuntimeError("Name is not valid!")
        self.__name = value

    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks():
        ...
    
    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.__storage.block_size
    
    @abstractmethod
    def clear():
        ...
    
class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__blocks = []

    def grow(self, block_count):
        self.__blocks += self.storage.allocate(block_count)
    
    @property
    def size_in_blocks(self):
        return len(self.__blocks)
    
    def clear(self):
        self.storage.free(self.__blocks)
        self.__blocks = []

class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []
    
    def add(self, entity: Entity):
        self.__children += [entity]

    @property
    def size_in_blocks(self):
        total_size = 0
        for child in self.__children:
            total_size += child.size_in_blocks
        return total_size
    
    def clear(self):
        for child in self.__children:
            child.clear()



#Testing ground
my_ssd = StorageDevice(block_count=1000, block_size=4096)
folder = Directory(my_ssd, 'newfolder')
file1 = File(my_ssd, 'foogletoogan')
file2 = File(my_ssd, 'file2')

folder.add(file1)
folder.add(file2)

file1.grow(99)
file2.grow(899)
print('file size:')
print('file 1:',file1.size_in_bytes)
print('file 2:',file2.size_in_bytes)

print(folder.size_in_blocks, '\n')

print(f'after clearing folder')
folder.clear()
print('file 1:',file1.size_in_bytes)
print('file 2:',file2.size_in_bytes)