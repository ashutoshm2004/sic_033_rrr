class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            

    def add_at_pos(self, data, position):
        nn = Node(data)
        if position == 0:
            nn.next = self.head
            self.head = nn

        else:
            temp = self.head
            count = 0
            while temp is not None and count < position-1:
                temp = temp.next
                count += 1
            if temp is None:
                print("Position out of range")
                return 
            nn.next = temp.next
            temp.next = nn

if __name__ == '__main__':
    ll = Linkedlist()
    ll.add_at_pos(5,0)
    ll.add_at_pos(10,1)
    ll.add_at_pos(15,2)
    ll.add_at_pos(20,3)
    ll.add_at_pos(25,1)
    ll.display()
