import hashlib
from typing import Union

class HashMapArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.hash = hashlib.sha256()
        
    def add_new_element(self, key : str, value : Union[str, int, float] ):
        self.hash.update(key.encode())
        hash_hex = self.hash.hexdigest()
        index = int(hash_hex, 16) % self.size

        if self.array[index]:
            print('steve')
        else:
            self.array[index] = value

        


    
        

a = HashMapArray(100)
a.add_new_element('igor', 19)
a.add_new_element('pedro', 'gay')
a.add_new_element('lucas', 30.2)
print(a.array)