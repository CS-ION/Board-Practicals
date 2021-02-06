import pickle

print('''MENU DRIVEN PROGRAM
1. Adding a new record (EID, Ename, designation, salary)
2. Display the detail of all employees whose designation is salesman
ENTER YOUR CHOICE (1/2/3/4/5)''')

def CreateEmp():
    f = open('emp.dat','ab+')
    r = int(input('Enter the total number of records\nEnter 0 if you dont want to enter any : '))
    for I in range(r):
        EID = input('enter EID : ')
        Ename = input('enter name : ')
        designation = input('enter designation : ')
        salary = float(input('enter salary : '))
        T = (EID, Ename, designation, salary)
        pickle.dump(T,f)
    f.close()
    print('Operation done succesfully')

def show():
    f = open('emp.dat','rb')
    try:
        while True:
            T = pickle.load(f)
            if T[2].lower() == 'salesman':
                print(T)
    except EOFError:
        f.close()

while True:
    print('''\nENTER YOUR CHOICE (1/2)'
PRESS ANY OTHER KEY TO EXIT''')
    choice = input()
    print('\n')
    if choice == '1':
        CreateEmp()
    elif choice == '2':
        show()
    else:
        raise SystemExit