
class Node:
    def __init__(self, name, score):
        self.data = str(name) + ", " + str(score)
        self.next = None
        self.pre = None
        self.name = name
        self.score = score

    def getData(self):
        return self.data

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getNext(self):
        return self.next

    def getPre(self):
        return self.pre

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPre(self, newpre):
        self.pre = newpre

class Golf_score:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, name, score):

        newnode = Node(name, score)
        if self.first is None and self.last is None:
            self.first = newnode
            self.last = newnode
        else:

            if newnode.getScore() <= self.first.getScore():
                newnode.setNext(self.first)
                self.first.setPre(newnode)
                self.first = newnode

            elif newnode.getScore() >= self.last.getScore():
                newnode.setPre(self.last)
                self.last.setNext(newnode)
                self.last = newnode

            else:

                current = self.first

                while current.score <= self.last.score:
                    next_node = current.next

                    if newnode.score >= current.score\
                        and newnode.score <= next_node.score:
                        newnode.setPre(current)
                        newnode.setNext(next_node)
                        current.setNext(newnode)
                        next_node.setPre(newnode)
                        break

                    current = current.next

    def update(self, name, score):

        self.remove(name)
        self.add(name, score)

    def remove(self, name):
        current = self.first
        previous = None
        found = False

        while found is False:
            if current.name == name:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.first = current.getNext()

        else:
            previous.setNext(current.getNext())

    def print_ascend(self):

        value = self.first

        while value is not None:
            print(str(value.getData()))
            value = value.getNext()

    def print_descend(self):

        value = self.last

        while value is not None:
            print(str(value.getData()))
            value = value.getPre()

    def same_score(self, name):

        node = self.first
        name_score = 0

        while node is not None:
            if node.name == name:
                name_score = node.score
                break
            node = node.getNext()

        node = self.first

        while node is not None and node.score <= name_score:
            if node.score == name_score:
                print(node.data)
            node = node.getNext()

    def print_linked(self):

        value = self.first

        while value is not None:
            print(str(value.getData()))
            value = value.getNext()

golf_score = Golf_score()
golf_score.add("Alex", 5)
golf_score.add("Jane", 2)
golf_score.add("Tim", 5)
golf_score.add("Pam", 10)
golf_score.add("Josh", 5)
golf_score.add("Noona", 10)
golf_score.add("L", 0)
golf_score.print_ascend()
print("==================================")
golf_score.print_descend()
print("==================================")
golf_score.same_score("Josh")
print("==================================")
golf_score.same_score("Pam")
print("==================================")
golf_score.remove("Pam")
golf_score.print_linked()
print("==================================")
golf_score.update("Josh", 2)
golf_score.print_linked()

