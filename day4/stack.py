import sys

class Stack:
    def __init__(self, size=5):
        self.stk = []
        self.size = size
        print('Empty Stack is created!')

    def push(self):
        if len(self.stk) == self.size:
            print('Stack is full')
            return
        element = input('Enter the element to be pushed: ')
        self.stk.insert(0, element)

    def pop(self):
        if not self.stk:
            print('Stack is empty')
            return
        print(f'Popped element is {self.stk[0]}')
        del self.stk[0]

    def list_stack(self):
        if not self.stk:
            print('Stack is empty')
            return
        print('Stack is: ', self.stk)

    
class Menu:
    def __init__(self, stack):
        pass

    def get_menu(self, stack):
        menu={
            1: stack.push,
            2: stack.pop,
            3: stack.list_stack,
            4: self.end_of_program
        }
        return menu
    
    def run_menu(self, stack):
        while True:
            choice = int (input("1.Push 2.Pop 3.Display 4.Exit Your choice: "))
            menu = self.get_menu(stack)
            menu.get(choice, self.invalid_choice)()
        print("~End~")

    def invalid_choice(self):
        print("Try again!")

    def end_of_program(self):
        sys.exit("End of Program")


stack = Stack()
menu = Menu(stack)
menu.run_menu(stack)



# num=[2,5,7,3,1,9,4,0]
# print(num.sort())
# print(sorted(num))