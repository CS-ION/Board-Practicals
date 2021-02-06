import pickle

print('''MENU DRIVEN PROGRAM
1. Adding a new book [BookNo, Book_Name, Author, Price]
2. UDF which accepts the Author name as parameter
and count and return number of books by the given Author
ENTER YOUR CHOICE (1/2/3/4/5)''')

def CreateFile():
    f = open('Book.dat','ab+')
    r = int(input('Enter the total number of books\nEnter 0 if you dont want to enter any : '))
    for I in range(r):
        BookNo = int(input('enter BookNo : '))
        Book_Name = input('enter book name : ')
        Author = input('enter author name : ')
        Price = float(input('enter price : '))
        T = [BookNo, Book_Name, Author, Price]
        pickle.dump(T,f)
    f.close()
    print('Operation done succesfully')

def CountRec(Author):
    f = open('Book.dat','rb')
    try:
        c = 0
        while True:
            T = pickle.load(f)
            if T[2].lower() == Author:
                c+=1
    except EOFError:
        f.close()
    print(f'Books written by {Author.upper()} = {c}')

while True:
    print('''\nENTER YOUR CHOICE (1/2)'
PRESS ANY OTHER KEY TO EXIT''')
    choice = input()
    print('\n')
    if choice == '1':
        CreateFile()
    elif choice == '2':
        Author = input('Enter author name : ').lower()
        CountRec(Author)
    else:
        raise SystemExit