class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.size = 0

    def push(self, item, priority):
        self.pq.append((priority, item))
        self.size += 1
        self._upheap(self.size - 1)

    def pop(self):
        if self.size == 0:
            raise Exception('Queue is empty.')
        self.size -= 1
        top = self.pq[0]
        self.pq[0] = self.pq[self.size]
        self.pq.pop()
        self._downheap(0)
        return top[1]

    def _upheap(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.pq[parent][0] > self.pq[index][0]:
            self.pq[index], self.pq[parent] = self.pq[parent], self.pq[index]
            index = parent
            parent = (index - 1) // 2

    def _downheap(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < self.size and self.pq[left][0] > self.pq[largest][0]:
            largest = left
        if right < self.size and self.pq[right][0] > self.pq[largest][0]:
            largest = right
        if largest != index:
            self.pq[index], self.pq[largest] = self.pq[largest], self.pq[index]
            self._downheap(largest)


