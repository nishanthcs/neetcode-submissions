import random
class RandomizedSet:

    def __init__(self):
        # Value -> Index
        self.set_storage: dict[int,int] = {}
        
        # Index -> Value
        self.quick_lookup: list[int] = []
        

    def insert(self, val: int) -> bool:
        if val in self.set_storage:
            return False

        # O(1)
        self.quick_lookup.append(val)
        
        # O(1) Appended to the last
        self.set_storage[val] = len(self.quick_lookup)-1

        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.set_storage:
            return False
        
        del_index = self.set_storage[val]
        
        quick_lookup_last_val = self.quick_lookup[-1]

        # Replace the value with the last value from quick lookup
        self.quick_lookup[del_index] = quick_lookup_last_val
        # Update the index of the last value 
        self.set_storage[quick_lookup_last_val] = del_index
        # Remove the last value from quicklookup
        self.quick_lookup.pop()

        del self.set_storage[val]
        
        return True

        
    def getRandom(self) -> int:
        return random.choice(self.quick_lookup)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()