
class Stack:
    def __init__(self):
        self.list = []
        self.top = -1

    def push(self, ele):
        self.list.append(ele)
        self.top += 1

    def pop(self):

        if self.top >= 0:
            self.top -= 1
            index = self.top + 1
            value = self.list[index]
            self.list.remove(value)
            return value

        else:

            check = "Error: no element to be found"
            return check

    def peek(self):

        if self.top >= 0:
            return self.list[self.top]

        else:

            check = "Error: no element to be found"
            return check

    def is_empty(self):

        if self.top < 0:
            check = True

        else:
            check = False

        return check

    def size(self):

        if self.top < 0:
            num = 0

        else:
            num = self.top + 1

        return num

    def contain(self, ele):
        if ele in self.list:
            check = True
        else:
            check = False

        return check


class Valetpark:
    def __init__(self, n1, n2):
        self.soi_1 = Stack()
        self.soi_2 = Stack()
        self.soi_limit1 = n1
        self.soi_limit2 = n2

    def park(self, car):

        if self.soi_limit1 > 0:
            self.soi_1.push(car)
            self.soi_limit1 -= 1

            return self.soi_1.list, self.soi_2.list

        elif self.soi_limit2 > 0:
            self.soi_2.push(car)
            self.soi_limit2 -= 1

            return self.soi_1.list, self.soi_2.list

        else:
            print("The parking lot is full")

    def get(self, car):

        check = True

        if self.soi_1.contain(car) is True:
            while self.soi_1.peek() != car:

                if self.soi_limit2 <= 0:
                    check = False
                    break
                else:
                    self.soi_2.push(self.soi_1.pop())
                    self.soi_limit2 -= 1
                    self.soi_limit1 += 1

            if check is False:
                print("Cannot get the car out")

            else:

                self.soi_1.pop()
                return self.soi_1.list, self.soi_2.list

        elif self.soi_2.contain(car) is True:
            while self.soi_2.peek() != car:

                if self.soi_limit1 <= 0:
                    check = False
                    break
                else:
                    self.soi_1.push(self.soi_2.pop())
                    self.soi_limit1 -= 1
                    self.soi_limit2 += 1

            if check is False:
                print("Cannot get the car out")

            else:

                self.soi_2.pop()
                return self.soi_1.list, self.soi_2.list

        else:
            print("There is no car with that ID")

    def __str__(self):
        return str(self.soi_1.list) + str(self.soi_2.list)


sample = Stack()

print(sample.list)
sample.push(1)
print(sample.list)
print(sample.size())
print(sample.contain(3))
print(sample.contain(1))
print(sample.is_empty())
print(sample.list)

park = Valetpark(5, 6)

park.park("166")
park.park("167")
park.park("165")
park.park("161")
park.park("106")
park.park("10")
park.park("190")
# park.park("186")
# park.park("15")
# park.park("12")

# park.park("156")

print("=================================================")
print(park.soi_1.list, park.soi_2.list)
park.get("161")
print(park)
park.get("10")
print(park.__repr__())
# print(park.soi_1.list, park.soi_2.list)
# park.get("955")
# print(park.soi_1.list, park.soi_2.list)
# park.get("166")
# print(park.soi_1.list, park.soi_2.list)
