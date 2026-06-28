import time
class RandomizedSet:

    def __init__(self):
        self.nums = {}
        

    def insert(self, val: int) -> bool:
        if self.nums.get(val):
            return False
        self.nums[val] = val

        return True
        

    def remove(self, val: int) -> bool:
        val = self.nums.pop(val, None)
        if not val:
            return False
        
        return True

        

    def getRandom(self) -> int:
        keys = list(self.nums.keys())

        epoch_time = int(time.time())

        if len(keys) == 1:
            random_idx = 0 
        else:
            random_idx = epoch_time % (len(keys)-1)

        return self.nums.get(keys[random_idx])




        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()