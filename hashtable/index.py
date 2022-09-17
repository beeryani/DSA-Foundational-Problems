'''
Implementation of Hash Table in Python based on the GeeksForGeeks article
'''

from numpy import record


class HashTable:
    def __init__(self, size):
        self.size = size;
        self.hash_table = self.create_buckets()
    # main function to create buckets within the __init__ class
    def create_buckets(self):
        return [[] for i in range(self.size)]
    #Insertion of values in hash table

    def insert_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

  
    

hash_table = HashTable(50)


# learning about enumerate function

L1 = ["eat", "sleep", "repeat"];
found_Key = False;
key = 10;
for index, record in enumerate(L1):
    record_key, record_value = index, record

    if record_key == key:
        found_Key = True
        break
    

