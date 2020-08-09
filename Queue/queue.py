class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue_size != 0:
            first_item = self.queue[0]
            del self.queue[0]
            return first_item
        else:
            return -1

    def peek(self):
        if self.queue == []:
            return None
        return self.queue[0]
    
    def queue_size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(21)
print(queue.peek())
print(queue.queue_size())
