filename = input('Enter the name of text file : ')

print('''\nMENU DRIVEN PROGRAM
a. Count and display the number of upper case and 
lower case characters in the file. Display whether 
the file contains more number of upper case or 
lower case characters and by how much.
b. Create a new file which contains all the lines 
of the first file starting with P. Also display 
the number of lines in the second file.\n''')

def up_lw(f):
    up,lw = 0,0
    for I in f.readlines():
        for J in I:
            if J.isupper():
                up +=1
            elif J.islower():
                lw +=1
    print(f'Uppercase : {up}')
    print(f'Lowercase : {lw}')
    if up > lw :
        print('Uppercases more than Lowercases')
    else :
        print('Lowercases more than Uppercases')
    f.close()

def new_file(f):
    f1 = open('new_file.txt','w')
    lines = 0
    for I in f.readlines():
        if I[0] == 'P':
            lines +=1
            f1.write(I)
    print(f'No of lines of new_file : {lines}')
    f.close()
    f1.close()

while True:
    print('''\nENTER YOUR CHOICE (a/b)'
PRESS ANY OTHER KEY TO EXIT''')
    choice = input()
    print('\n')
    if choice == 'a':
        up_lw(open(f'{filename}.txt','r'))
    elif choice == 'b':
        new_file(open(f'{filename}.txt','r'))
    else:
        raise SystemExit