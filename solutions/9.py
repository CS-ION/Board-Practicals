import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="isgsql",database="test")
mycursor=mydb.cursor()

def Fetch70000():
    mycursor.execute("Select * from EMP where EmpSalary>70000")
    records=mycursor.fetchall()
    for x in records:
        print(x)
        
def Update1000():
    mycursor.execute("Update EMP set EmpSalary=EmpSalary+1000 where EmpSalary<80000")
    mydb.commit()

def DeleteSalary():
    Salary=int(input("enter salary of employee whose records you want to delete"))
    mycursor.execute("delete from EMP where EmpSalary=Salary")
    mydb.commit()
    print(mycursor.rowcount,"record deleted")

def DisplayAsc():
    mycursor.execute("Select * from EMP order by EmpSalary")
    records=mycursor.fetchall()
    for x in records:
        print(x)

def DeleteInput():
    Name=input("enter name of employee whose records you want to delete")
    mycursor.execute(f'delete from EMP where EmpName={Name}')
    mydb.commit()
    print(mycursor.rowcount,"record deleted")

print("The commands that the system can execute are as follows-")
print("1 to read and fetch all the records from EMP table having salary more than 70000 ")
print("2 to update the records of employees by increasing salary by  1000 of all those employees who are getting less than  80000")
print("3 to delete the record on the basis of inputted salary")
print("4 to display all records in ascending order of their salary")
print("5 to delete the employee record whose name is read from the keyboard at execution time")

while True:
    Choice=input("Enter the number for the command you wish to fulfil: ")
    if Choice==1:
        Fetch70000()
    elif Choice==2:
        Update1000()
    elif Choice==3:
        DeleteSalary()
    elif Choice==4:
        DisplayAsc()
    elif Choice==5:
        DeleteInput()
    else:
        print("wrong command, retry")
        continue
    Continue=input("Do you wish to continue? (Y/N)")
    if Continue =="N" or Continue=="n":
        print("Thank you")
        break

