def CountRec():
    f = open('STUDENT.dat','rb')
    try:
        c = 0
        while True:
            T = pickle.load(f)
            if T[2]>75:
                c+=1
    except EOFError:
        f.close()
    print(f'No of students scoring above 75% = {c}')

CountRec()