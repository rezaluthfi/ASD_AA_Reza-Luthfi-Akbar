class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def insertFirst (self, data):
        newNode = Node(data)    
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            

    def insertLast (self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode 

    def deleteFirst (self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def deleteLast (self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.deleteFirst()
                elif current == self.tail:
                    self.deleteLast()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    
    def displayList (self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def find(self, data):
        current = self.head
        isFound = False
        while current is not None:
            if current.data == data:
                print(f'{data} ditemukan')
                isFound = True
                break
            else:
                current = current.next
        if isFound == False:
            print(f'{data} tidak ditemukan')




dll = DoublyLinkedList()
print("Find:")
dll.insertLast(10)
dll.insertLast(12)
dll.insertFirst(15)
dll.find(12)






# dll = DoublyLinkedList()
# print("Display List:")
# dll.insertLast(10)
# dll.insertLast(12)
# dll.insertFirst(15)
# dll.insertFirst(20)
# dll.displayList()



# dll = DoublyLinkedList()
# print("Delete:")
# dll.insertLast(10)
# dll.insertLast(12)
# dll.insertFirst(15)
# dll.insertFirst(20)
# dll.delete(20)
# print(dll.tail.data)



# dll = DoublyLinkedList()
# print("Delete Last:")
# dll.insertLast(5)
# dll.insertLast(7)
# dll.insertLast(9)
# dll.deleteLast()
# print(dll.tail.data)

# print("Insert First:")
# dll.insertFirst(2)
# dll.insertFirst(4)
# dll.insertFirst(6)
# dll.insertFirst(10)
# print(dll.head.data)

# print("Insert Last:")
# dll.insertLast(1)
# dll.insertLast(3)
# dll.insertLast(5)
# dll.insertLast(8)
# print(dll.tail.data)



# print("Delete First:")
# dll.insertFirst(2)
# dll.insertFirst(4)
# dll.insertFirst(6)
# dll.deleteFirst()
# print(dll.head.data)





# dll.displayList()  