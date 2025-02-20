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

    def other_choice():
        print("Try again!")

    menu={
        1: monday,
        2: tuesday,
        3: wednesday,
        4: thursday,
        5: friday
    }

    while True:
        choice = int (input("1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday Your choice: "))
        if choice == -1:
            break
        menu.get(choice, other_choice)()
    print("~End~")
        