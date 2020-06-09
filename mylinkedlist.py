# 10-->5-->16

# myLinkedList = {
# 	head: {
# 		value: 10,
# 		nextt: {
# 			value: 5,
# 			nextt: {
# 				value: 16,
# 				nextt: None
# 			}
# 		}
# 	}
# }


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printLL(self):
        LL = []
        current = self.head
        while current != None:
            LL.append(current.data)
            current = current.next
        print(LL)


LL = LinkedList()

LL.append(0)
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.prepend(20)

LL.printLL()
