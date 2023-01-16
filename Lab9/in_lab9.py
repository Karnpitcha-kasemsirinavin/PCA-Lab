class Node:
    def __init__(self, username_in, password_in):

        self.left = None
        self.right = None
        self.username = username_in
        self.password = password_in


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if new_node.username <= current_node.username:
            if current_node.left is not None:
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.username > current_node.username:
            if current_node.right is not None:
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find(self, username):
        return self.__find_node(self.root, username)

    def __find_node(self, current_node, username):
        """start from current_node = self.root"""

        if current_node is not None:
            if current_node.username == username:
                return current_node.username, current_node.password
            else:
                if username < current_node.username:
                    return self.__find_node(current_node.left, username)
                elif username > current_node.username:
                    return self.__find_node(current_node.right, username)

    def find_min(self, current_node):

        if current_node.left is None:
            return current_node
        else:
            return self.find_min(current_node.left)

    def is_empty(self):

        if self.root is None:
            return True
        else:
            return False

    def preorder(self, current_node):

        if current_node is None:
            return
        else:
            print(current_node.username, end="  ")

            if current_node.left is not None:
                self.preorder(current_node.left)

            if current_node.right is not None:
                self.preorder(current_node.right)

    def inorder(self, current_node):

        if current_node is None:
            return
        else:
            if current_node.left is not None:
                self.inorder(current_node.left)

            print(current_node.username, end="  ")

            if current_node.right is not None:
                self.inorder(current_node.right)

    def postorder(self, current_node):

        if current_node is None:
            return
        else:
            if current_node.left is not None:
                self.postorder(current_node.left)
            if current_node.right is not None:
                self.postorder(current_node.right)

            print(current_node.username, end="  ")

    def print_tree(self, current_node, level):

        if current_node.right is not None:
            self.print_tree(current_node.right, level+1)
        print(' '*3*level, end="")
        print(current_node.username)
        if current_node.left is not None:
            self.print_tree(current_node.left, level+1)


sample = BST()
sample.insert(Node('p', 1234))
sample.insert(Node('h', 644))
sample.insert(Node('b', 498))
sample.insert(Node('z', 498))
sample.insert(Node('i', 498))
sample.print_tree(sample.root, 0)
# sample.remove('h')
# sample.remove('z')
# sample.remove('p')

print("==================")
sample.print_tree(sample.root, 0)
# find
print(sample.find('b'))
print(sample.find_min(sample.root))

# current = sample.root
#
# while current is not None:
#     print(current.username)
#     current = current.left

# print(sample.root.username)
# print(sample.root.right.username)
# print(sample.root.left.username)
# print(sample.root.left.right.username)

sample.preorder(sample.root)
print()
print("==============")
sample.postorder(sample.root)
print()
print("==============")
sample.inorder(sample.root)
print()
print("==============")
sample.print_tree(sample.root, 0)
