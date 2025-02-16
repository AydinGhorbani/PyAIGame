#    Main Author(s): Aydin Ghorbani
#    Main Reviewer(s): Professor Adarsh Sehgal

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table
class HashTable:
    def __init__(self, capacity=32):
        self._capacity = capacity  
        self.size = 0
        self.buckets = [[] for _ in range(self._capacity)]
    
    def hash_function(self, key):
        return hash(key) % self._capacity
    
    def load_factor(self):
        return self.size / self._capacity
    
    def resize(self):
        old_buckets = self.buckets
        self._capacity *= 2
        self.buckets = [[] for _ in range(self._capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)
    
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return False
        bucket.append((key, value))
        self.size += 1
        if self.load_factor() > 0.7:
            self.resize()
        return True
    
    def modify(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True
        return False
    
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False
    
    def search(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def capacity(self):
        return self._capacity
    
    def __len__(self):
        return self.size
