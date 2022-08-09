// https://leetcode.com/problems/design-hashmap

      
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def update(self, key, value):
        found = False
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                self.bucket[i] = [key, value]
                found = True
                break
        if not found:
            self.bucket.append([key, value])
                
    def get(self, key):
        for k in self.bucket:
            if k[0] == key:
                return k[1]
        return -1

    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                del self.bucket[i]

class MyHashMap:

    def __init__(self):
        self.maxLen = 100000
        self.hTable = [Bucket() for i in range(self.maxLen)]

    def put(self, key: int, value: int) -> None:
        index = key % self.maxLen
        self.hTable[index].update(key, value)
        
    def get(self, key: int) -> int:
        index = key % self.maxLen
        return self.hTable[index].get(key)

    def remove(self, key: int) -> None:
        index = key % self.maxLen
        self.hTable[index].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)