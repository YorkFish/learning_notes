class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())

    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())