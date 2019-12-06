class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head

        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self._head

        while cur:
            print(cur.item)
            cur = cur.next
        return None

    def add_first(self, item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = SingleNode(item)

        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add_first(item)
        elif (self.length() - 1) < pos:
            self.append(item)
        else:
            node = SingleNode(item)

            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    lst = SingleLinkList()
    
    lst.add_first(10)
    lst.add_first(20)
    lst.append(30)
    lst.insert(2, 40)
    print(f"Length of lst is {lst.length()}")
    lst.traverse()
    
    print(lst.search(30))
    print(lst.search(31))

    lst.remove(20)
    print(f"Length of lst is {lst.length()}")
    lst.traverse()
