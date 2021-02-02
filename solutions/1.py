import pickle

def initial():
    try:
        f = open('STUDENT.dat','ab+')
    except:
        return
    r = int(input('Enter the total number of children\nEnter 0 if you dont want to enter any : '))
    for I in range(r):
        roll_no = int(input('enter roll no : '))
        name = input('enter name : ')
        marks = float(input('enter marks : '))
        T = (roll_no,name,marks)
        pickle.dump(T,f)
    f.close()

initial()

print('''\nMENU DRIVEN PROGRAM
a. displaying the details of all students
b. searching a student using roll no\n''')

def search():
    f = open('STUDENT.dat','rb')
    roll_no = int(input('enter the roll no : '))
    try:
        while True:
            T = pickle.load(f)
            if T[0] == roll_no:
                return T 
    except EOFError:
        return 'RECORD NOT FOUND'
    f.close()

def display():
    f = open('STUDENT.dat','rb')
    try:
        c = 1
        while True:
            T = pickle.load(f)
            print(c,T) 
            c+=1
    except EOFError:
        f.close()
    if c == 1:
        print('NO RECORDS FOUND')

while True:
    print('''\nENTER YOUR CHOICE (a/b)'
PRESS ANY OTHER KEY TO EXIT''')
    choice = input()
    print('\n')
    if choice == 'b':
        print(search())
    elif choice == 'a':
        display()
    else:
        raise SystemExit