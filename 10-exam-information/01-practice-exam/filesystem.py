# Enter your code here:
class StorageDevice:
    def __init__(self, block_count: int, block_size: int) -> None:
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return sum(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return sum(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return (sum(self.__available_blocks) + sum(self.__used_block_count))
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count: int, ) -> list:
        if block_count > len(self.__available_blocks):
            raise RuntimeError()
        
        allocated_blocks = list(self.__available_blocks)[:block_count]
        for block in allocated_blocks:
            self.__available_blocks.remove(block)
            self.__used_blocks.add(block)

        return allocated_blocks
    
    def free(self, blocks: list) -> None:
        if blocks not in list(self.__used_blocks):
            raise RuntimeError()
        
        for block in blocks:
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)
        

storage = StorageDevice(block_count=10, block_size=5)

print(storage.allocate(3))
print(storage.allocate(5))