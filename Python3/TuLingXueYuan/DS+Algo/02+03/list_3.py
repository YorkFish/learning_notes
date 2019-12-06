class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def traverse(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def add_first(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add_first(item)
        elif self.length() - 1 < pos:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            cnt = 0
            while cnt < pos - 1:
                cur = cur.next
                cnt += 1
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next is None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            cur = cur.next
            while cur:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next


if __name__ == "__main__":
    lst = DLinkList()

    lst.add_first(2)
    lst.add_first(1)
    lst.append(4)
    lst.append(5)
    lst.insert(0, 0)
    lst.insert(3, 33)
    print(f"length: {lst.length()}")
    lst.traverse()

    print(lst.search(3))
    print(lst.search(5))

    lst.remove(33)
    print(f"length: {lst.length()}")
    lst.traverse()
