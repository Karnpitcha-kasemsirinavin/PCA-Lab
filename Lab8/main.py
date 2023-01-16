
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        self.head = None
        return self.head

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while found is False:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def squish(self):

        check_value = self.head
        previous = None
        n = self.size()

        for num in range(n-1):

            if check_value.getData() == check_value.getNext().getData():
                previous = check_value
                check_value = check_value.getNext()
                previous.setNext(check_value.getNext())
                check_value = previous
            else:
                check_value = check_value.getNext()


    def dble(self):

        current_value = self.head

        while current_value is not None:

            value = current_value.getData()
            newnode = Node(value)
            newnode.setNext(current_value.getNext())
            current_value.setNext(newnode)
            current_value = current_value.next.next


    def print_linked(self):

        value = self.head

        while value is not None:
            # string += str(value.getData())
            print(str(value.getData()))
            print(id(value.data)) #for id
            value = value.getNext()

a = UnorderedList()
a.add(0)
a.add(1)
a.add(1)
a.add(3)
a.add(3)
a.add(3)
a.add(0)
a.add(0)
a.add(0)
a.add(1)
a.add(1)
a.add(0)
a.add(0)
a.add(0)
a.add(0)

a.print_linked()
print("============")
a.squish()
a.print_linked()
print("============")
a.dble()
a.print_linked()
# print(a.head.getData())


