def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def sum(list):
    sum=0
    for a in list:
        sum+=a
    return sum

def multiplication(list):
    multi=1
    for a in list:
        multi*=a
    return multi

def smallest(list):
    smallest=list[0]
    for a in list:
        if a<smallest:
            smallest=a
    return smallest

def largest(list):
    largest=list[0]
    for a in list:
        if a>largest:
            largest=a
    return largest

def seclargest(list):
    largest1=list[0]
    seclargest=list[1]
    for a in list:
        if a>largest1:
            seclargest=largest1
            largest1=a
        elif a>seclargest:
            seclargest=a
        else:
            None
    return seclargest

choice=0

while choice!=6:
    print("Plese choose from one of the following options")
    print("1)Returning the sum")
    print("2)Returning the mulpilication")
    print("3)Returning the smallest element")
    print("4)Returing the largest element")
    print("5)Returing the seclargest")
    print("6)In order to exit the program")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        list=eval(input("Enter the list"))
        print("The sum of the given list:",sum(list))
        space()
    
    elif choice==2:
        space()
        list=eval(input("Enter the list"))
        print("The multiplication of the given list:",multiplication(list))
        space()
        
    elif choice==3:
        space()
        list=eval(input("Enter the list"))
        print("The smallest number is:",smallest(list))
        space()
        
    elif choice==4:
        space()
        list=eval(input("Enter the list"))
        print("The largest number is:",largest(list))
        space()
        
    elif choice==5:
        space()
        list=eval(input("Enter the list"))
        print("The second largest number is:",seclargest(list))
        space()
            

