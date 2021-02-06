Arr = [1,2,3,4,5]

def push(Arr):
    stack = []
    for I in Arr[::-1]:
        if I%5 == 0:
            stack.append(I)
    if stack == []:
        print('Underflow alert : No element div by 5')
    else:
        print(stack)

def pop(Arr):
    if Arr == []:
        print('Underflow alert')
        return
    print('Element removed : ',Arr.pop())

print('''CHOOSE YOUR OPERATION BY TYPING THE NUMBER
    1. PUSH INTO stack
    2. POP FROM Arr
    Press any other key to exit''')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        push(Arr)
    elif choice == '2':
        pop(Arr)
    else:
        raise SystemExit