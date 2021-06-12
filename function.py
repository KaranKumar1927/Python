def sayHello():
    print("Hello " + name)

def greetings(newname):
    print("Hello " + newname)

def sum(x,y):
    return x+y

#main program
name = input("Enter your name \n")#name is a global variable 
sayHello()
def main():
    

    newName = input("enter the name again")#newName has a local scope
    greetings(newName)

    print(str(sum(10,20)))

main()   