class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index >= self.length:
            self.append(data)
        new_node = Node(data)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = new_node
        new_node.next = follower
        new_node.prev = leader
        follower.prev = new_node
        self.length += 1

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def remove(self, index):
        if index >= self.length:
            print('ERRROOOOORR')
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader.next
        leader.next = unwantedNode.next
        self.length -= 1

    # def my_reverse(self):
    #     first = self.head
    #     self.tail = self.head
    #     second = first.next
    #     while second:
    #         third = second.next
    #         second.next = first
    #         first = second
    #         second = third
    #     self.head.next = None
    #     self.head = first

    def reverse(self):
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))


LL = LinkedList()
LL.append(3)
LL.append(4)
LL.append(5)
LL.prepend(6)
LL.insert(2, 99)
LL.printl()
LL.remove(1)
LL.printl()
LL.reverse()
LL.printl()
