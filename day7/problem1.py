class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

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
    while True:
        ch = int (input("\nEnter 1 to enter data 0 to stop 2 to display: "))
        match ch:
            case 1:
                data, position = map(int, input("Enter the data and position: ").split())
                ll.add_at_pos(data, position)
            case 0:
                break
            case 2:
                ll.display()
            case _:
                print("Try again!")
            
        