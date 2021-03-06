class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """ 走的是完全二叉树的路 """
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):
        if root is None:
            return

        print(root.elem, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.lchild)
        print(root.elem, end=' ')
        self.inorder(root.rchild)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=' ')

    def breath_traverse(self, root):
        if root is None:
            return

        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem, end=' ')
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        print()


if __name__ == "__main__":
    tree = Tree()

    for i in range(10):
        tree.add(i)

    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    tree.breath_traverse(tree.root)
