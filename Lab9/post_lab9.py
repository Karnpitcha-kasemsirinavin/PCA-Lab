class Node:
    def __init__(self, username_in, password_in):

        self.left = None
        self.right = None
        self.username = username_in
        self.password = password_in


class BST:

    trim_l = []

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
                return current_node
            else:
                if current_node is None:
                    return False
                else:
                    if username < current_node.username:
                        return self.__find_node(current_node.left, username)
                    elif username > current_node.username:
                        return self.__find_node(current_node.right, username)
        else:
            return "no node"

    def remove(self, username):

        if self.root is not None:
            if self.root.username == username:
                if self.root.right is not None:
                    pre_re = self.find_premin(self.root.right, self.root)
                    revalue = self.find_min(self.root.right)
                    if revalue.right is not None:
                        pre_re.left = revalue.right
                    else:
                        pre_re.left = revalue.left

                    revalue.left = self.root.left
                    if self.root.right != revalue:
                        revalue.right = self.root.right
                    else:
                        revalue.right = None
                    self.root = revalue
                else:
                    self.root = self.root.left
            else:
                if username < self.root.username:
                    self.__remove(self.root.left, self.root, username)
                elif username > self.root.username:
                    self.__remove(self.root.right, self.root, username)

    def __remove(self, node, pre_node, username):

        if node is None:
            return
        elif node.username == username:
            if pre_node.left is not None:
                if pre_node.left.username == username:
                    if node.right is not None:
                        revalue = self.find_min(node.right)
                        revalue.left = node.left
                        pre_node.left = revalue
                    else:
                        pre_node.left = node.left

            elif pre_node.right is not None:
                if pre_node.right.username == username:
                    if node.right is not None:
                        revalue = self.find_min(node.right)
                        pre_node.right = revalue
                    else:
                        pre_node.right = node.left
        else:
            if username < node.username:
                self.__remove(node.left, node, username)
            elif username > node.username:
                self.__remove(node.right, node, username)

    def find_min(self, current_node):

        if current_node.left is None:
            return current_node
        else:
            return self.find_min(current_node.left)

    def find_premin(self, current_node, pre_node):

        if current_node.left is None:
            return pre_node
        else:
            return self.find_premin(current_node.left, current_node)

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

        if current_node is not None:

            if current_node.right is not None:
                self.print_tree(current_node.right, level+1)
            print(' '*6*level, end="")
            print(current_node.username)
            if current_node.left is not None:
                self.print_tree(current_node.left, level+1)

    def store_data(self):

        file = open("users7.txt", "r")
        for line in file:
            line = line.strip()
            if len(line) > 1:
                username, password = line.split(" ")
                self.insert(Node(username, password))

    def count_num(self, current_node):

        if current_node is None:
            return 0

        return self.count_num(current_node.left) + self.count_num(current_node.right) + 1

    # def trim(self, min, max, current_node):
    #
    #     if current_node is not None:
    #
    #         if current_node.username < min or current_node.username > max:
    #
    #             self.remove(current_node.username)
    #
    #             if current_node.left is not None:
    #                 self.trim(min, max, current_node.left)
    #             if current_node.right is not None:
    #                 self.trim(min, max, current_node.right)
    #
    #
    #         else:
    #
    #             if current_node.left is not None:
    #                 self.trim(min, max, current_node.left)
    #             if current_node.right is not None:
    #                 self.trim(min, max, current_node.right)

    def trim(self, min_v, max_v):
        self.__trim(self.root, min_v, max_v)
        list_trim = BST.trim_l[::1]

        for value in list_trim:
            if value < min_v or value > max_v:
                self.remove(value)
                BST.trim_l.remove(value)

        return

    def __trim(self, root, min_v, max_v):

        if root:
            self.__trim(root.left, min, max)
            BST.trim_l.append(root.username)
            self.__trim(root.right, min_v, max_v)

sample = BST()
# sample.store_data()
# sample.print_tree(sample.root, 0)
# x = sample.count_num(sample.root)
# print(x)

sample.insert(Node("a", 659))
sample.insert(Node("k", 659))
sample.insert(Node("p", 659))
sample.insert(Node("d", 659))
sample.insert(Node("v", 659))
#
# sample.print_tree(sample.root, 0)
sample.print_tree(sample.root, 0)
print("=============================")
sample.trim("c", "v")
print("=============================")
# sample.store_data()
sample.print_tree(sample.root, 0)
print("=============================")

# login = True
# count = 3
# pre_user = ''
# while login is True:
#
#     user = input("Input username: ")
#     password = input("Input password: ")
#
#     node = sample.find(user)
#
#     if not node == "no node":
#
#         if user != pre_user:
#             count = 3
#
#         if node.password == password:
#             print("successful login")
#             count = 3
#             login = False
#         else:
#             if not count == 1:
#                 print("unsuccessful login due to the incorrect password")
#                 count -= 1
#                 print(str(count) + " attempts left")
#             else:
#                 print("unsuccessful login due to the incorrect password")
#                 print("You have been removed from the system")
#                 sample.remove(user)
#                 login = False
#     else:
#         print("That username is not in the system")
#
#     pre_user = user
#
# sample.print_tree(sample.root, 0)
