import heapq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_time = {}
        self.map = {}
        self.priority_queue = []
        self.update = set()
        self.time = 0
        

    def get(self, key: int) -> int:
        self.time += 1
        
        if key in self.map:
            f, t = self.freq_time[key]
            self.freq_time[key] = (f+1, self.time)
            self.update.add(key)
            return self.map[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity < 0:
            return 
        
        self.time += 1
        
        if key in self.map:
            f, t = self.freq_time[key]
            self.freq_time[key] = (f+1, self.time)
            self.update.add(key)
        
        else:
            if len(self.map) >= self.capacity:
                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)
                
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)
                
            self.freq_time[key] = (1, self.time)
            heapq.heappush(self.priority_queue, (1, self.time, key))
            self.update.add(key)

        self.map[key] =  value

# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(2)
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       #// returns 1
cache.put(3, 3);    #// evicts key 2
cache.get(2);       #// returns -1 (not found)
cache.get(3);       #// returns 3.
cache.put(4, 4);    #// evicts key 1.
cache.get(1);       #// returns -1 (not found)
cache.get(3);       #// returns 3
cache.get(4);       #// returns 4