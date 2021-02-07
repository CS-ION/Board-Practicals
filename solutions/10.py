stack = ['Bolivia','Cambodia','Azerbaijan']

def push(stack):
    x = input('Enter Country : ')
    stack.append(x)
    print('Country added : ',x)

def pop(stack):
    if stack == []:
        print('Underflow alert')
        return
    print('Country removed : ',stack.pop())

def display(stack):
    print(stack)

print('''CHOOSE YOUR OPERATION BY TYPING THE NUMBER
    1. PUSH INTO STACK
    2. POP FROM STACK
    3. DISPLAY STACK
    Press any other key to exit''')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        push(stack)
    elif choice == '2':
        pop(stack)
    elif choice == '3':
        display(stack)
    else:
        raise SystemExit
    