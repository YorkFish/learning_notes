class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycLinkedList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0

        cnt = 1
        cur = self._head
        while cur.next != self._head:
            cur = cur.next
            cnt += 1
        return cnt

    def traverse(self):
        if self.is_empty():
            return

        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)

    def add_first(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            self._head = node

    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):
        if pos <= 0:
            self.add_first(item)
        elif self.length() - 1 < pos:
            self.append(item)
        else:
            node = SingleNode(item)
            cur = self._head
            cnt = 0
            while cnt < pos - 1:
                cur = cur.next
                cnt += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return

        cur = self._head
        pre = None
        if cur.item == item:
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False

        cur = self._head
        if cur.item == item:
            return True

        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    lst = SingleCycLinkedList()

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
