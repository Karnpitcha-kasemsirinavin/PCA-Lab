class Node:
    def __init__(self, data):
        # your code here
        self.left = None
        self.right = None
        self.data = data

class BT:
    def __init__(self):
        self.root = None

    def insert(self, new_node):

        if self.root is None:
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if new_node.data <= current_node.data:
            if current_node.left is not None:
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node

        elif new_node.data > current_node.data:
            if current_node.right is not None:
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find_height(self, root):

        if root is None:
            return 0
        else:

            left_height = self.find_height(root.left)
            right_height = self.find_height(root.right)

            if right_height >= left_height:
                return right_height + 1
            else:
                return left_height + 1

    def size(self):
        node = self.root

        if node is None:
            return
        elif node is not None:
            return self.__size(node)

    def __size(self, node):
        if node is None:
            return 0
        else:
            return self.__size(node.left) + 1 + self.__size(node.right)

    def leaves_node(self):
        node = self.root
        if node is None:
            return

        elif node is not None:
            leaves_list = list()
            self.__leaves_node(node, leaves_list)
            return leaves_list

    def __leaves_node(self, node, leaves_list):

        if not node:
            return

        if node.left is None and node.right is None:
            leaves_list.append(node.data)
            return leaves_list
        if node.left is not None:
            self.__leaves_node(node.left, leaves_list)
        if node.right is not None:
            self.__leaves_node(node.right, leaves_list)


