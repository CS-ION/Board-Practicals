import pickle
import os 

def edit():
    f = open('phonebook.dat','rb')
    f1 = open('temp.dat','wb')
    existance = False
    try:
        while True:
            T = pickle.load(f)
            if T[0] == 'Arman':
                existance = True
                no = input('Enter new phone no : ')
                T = (T[0],no)
            pickle.dump(T,f1) 
    except EOFError:
        f.close()
        f1.close()
    os.remove('phonebook.dat')
    os.rename('temp.dat','phonebook.dat')
    if existance == False:
        print('Arman doesnt exist')
    elif existance == True:
        print('Operation done succesfully')