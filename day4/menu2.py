class Event:
    def monday(self):
        print('Today is Technical fest')

    def tuesday(self):
        print('Today is Cultural fest')

    def wednesday(self):
        print('Today is Sports fest')

    def thursday(self):
        print('Today is Ethnc day')

    def friday(self):
        print('Today is Half day')

    def other_choice(self):
        print("Try again!")

class Menu:
    def __init__(self, events):
        pass

    def get_menu(self, events):
        menu={
            1: events.monday,
            2: events.tuesday,
            3: events.wednesday,
            4: events.thursday,
            5: events.friday
        }
    
    def run_menu(self):
        while True:
            choice = int (input("1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday Your choice: "))
            if choice == -1:
                break
            menu.get(choice, events.other_choice)()
        print("~End~")


    
event = Event()
menu = Menu(event)
menu.run_menu()