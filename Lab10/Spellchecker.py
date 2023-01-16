class Hash:
    def __init__(self, path, tech):
        self.words = self.read(path)
        self.size = self.getprime(int(len(self.words) * 0.2))
        self.data = [None] * self.size
        self.loadfactor = 0
        self.collision = 0
        self.count_expand = 0
        self.tech = tech
        self.max = 0
        self.insert(self.words)

    def read(self, path):  # readfile

        with open(path) as file:
            words = file.read().split()
        return words

    def hash(self, str):  # hash word
        h = 0
        for c in str:
            h *= 5
            h += ord(c)
        return h

    def insert(self, words):
        for word in words:
            id = hash(word) % self.size  # find key
            if self.tech == 'linear':  # choose technique
                if self.data[id] is None:  # if that slot is empty put in
                    self.data[id] = word
                else:
                    self.linear(id, word)  # not empty call linear
                self.checkLoad()  # checking loadfactor
            elif self.tech == 'chain':
                if self.data[id] is None:
                    self.data[id] = Node(word)  # if empty assign Node
                    self.checkLoad()  # checking loadfactor
                else:
                    self.chain(id, word)  # not empty call chain

    def linear(self, id, word):
        self.collision += 1  # count collision
        while self.data[id] is not None:
            id += 1  # adding to make new key
            id %= self.size
        self.data[id] = word

    def chain(self, id, word):
        self.collision += 1  # count collision
        node = self.data[id]  # data at that slot
        count = 0
        while node.next is not None:
            count += 1
            node = node.next
        self.max = count if count > self.max else self.max  # assign new max value
        node.next = Node(word)  # assign new node after find none

    def checkLoad(self):  # for checking loadfactor
        self.loadfactor += 1
        if self.loadfactor / self.size > 0.5:  # loadfactor is more than half
            self.count_expand += 1  # count expansion
            temp = self.words[:self.loadfactor]  # current arr
            self.size = self.getprime(self.size * 2)
            self.data = [None] * self.size  # assign empty arr
            self.loadfactor = 0  # reset loadfactor
            self.insert(temp)  # insert old arr into new arr

    def isPrime(self, n):  # checking if that number is prime num or not
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if (n % i == 0):
                    return False
            return True
        else:
            return False

    def getprime(self, n):  # get next prime num
        while not self.isPrime(n):
            n += 1
        return n

    def search(self):  # search word
        input_w = input('Enter your word : ')
        if input_w in self.words:
            print('"{}" is correctly spelled'.format(input_w))
        else:
            suggest = []
            for word in self.words:
                wordLength = len(word)
                if wordLength == len(input_w):  # get word with same length
                    miss = 0
                    for i in range(wordLength):  # check miss alphabet
                        miss += 1 if input_w[i] is not word[i] else 0
                    if miss < 2:
                        suggest.append(word)  # add to suggest arr
            print('"{}" is not in the dictionary'.format(input_w))
            if len(suggest) > 0:
                print('Possible corrections are :', end=' ')
                for word in suggest:
                    print(word, end=' ')
                print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, node):
        self.next = node

    def __repr__(self):
        return self.data


# smallLinear = Hash('lab11/small.txt', 'linear')
fullLinear = Hash('full.txt', 'linear')


# smallChain = Hash('small.txt', 'chain')
# fullChain = Hash('full.txt', 'chain')

def stat(hash):
    print('Collision resolution :', hash.tech)
    print('Total words :', len(hash.words))
    print('{} expansions, load factors {}, {} collisions, longest chain {}'.format(hash.expand, hash.load / hash.size,
                                                                                   hash.crash, hash.max))
    print()


# stat(smallLinear)
# stat(fullLinear)
# stat(smallChain)
# stat(fullChain)

# smallLinear.search()
# fullLinear.search( )
print("collision:")
print(fullLinear.collision)
print(len(fullLinear.words))
print("expand:")
print(fullLinear.count_expand)
