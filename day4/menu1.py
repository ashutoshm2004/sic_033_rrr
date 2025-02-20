def monday():
    print('Today is Technical fest')

def tuesday():
    print('Today is Cultural fest')

def wednesday():
    print('Today is Sports fest')

def thursday():
    print('Today is Ethnc day')

def friday():
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
    choice = int (input("1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday Your Choice: "))
    if choice == -1:
        break
    menu.get(choice, other_choice)()
print("~End~")
    