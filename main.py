#WELCOME TO MY CALCULATOR SCRIPT!!

import os #THIS IMPORT IS FOR CLEAN THE CONSOLE WHEN IS NECESSARY

def sumn(): #SUM FUNCTION
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        sum =0
        print("ENTER NUMBERS TO BE ADDED ")
        print("FOR FINALIZE, ENTER 0")
        number = int(input("NUMBER: "))
        sum+= number
        while (number != 0):
            number = int(input("NUMBER: "))
            sum+= number
            print("CURRENT SUM: {}".format(sum))
        
        print("YOUR FINAL SUM IS: {}".format(sum))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def sub(): #SUBTRACTION FUNCTION
    try: 
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        subs =0
        print("ENTER NUMBERS TO BE SUBTRACTED ")
        print("FOR FINALIZE, ENTER 0")
        number = int(input("NUMBER: "))
        subs= number
        while (number != 0):
            number = int(input("NUMBER: "))
            subs-= number
            print("CURRENT SUBTRACTION: {}".format(subs))
        
        print("YOUR FINAL SUBTRACTION IS: {}".format(subs))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def multi(): #MULTIPLACTION FUNCTION
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        multip =1
        print("ENTER NUMBERS TO BE MULTIPLIED ")
        print("FOR FINALIZE, ENTER 0")
        number = int(input("NUMBER: "))
        multip*= number
        while (number != 0):
            number = int(input("NUMBER: "))
            if (number != 0): 
                multip*= number
            print("CURRENT MULTIPLICATION: {}".format(multip))

        print("YOUR FINAL MULTIPLICATION IS: {}".format(multip))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def divi(): #DIVISION FUNCTION
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        divis =0
        print("ENTER NUMBERS TO BE DIVIDED ")
        number = int(input("NUMBER: "))
        number2 = int(input("NUMBER: "))
        
        if (number2 == 0):
            print("DIVISION BY ZERO")
        else:
            divis = number/number2
            print("YOUR FINAL DIVISION IS: {}".format(divis))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def fibonnaci(): #FIBONACCI FUNCTION
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        cont = 2
        last,next_to_last = 1,0
        sum=0
        value = int(input("PLEASE ENTER A NUMBER FOR FIBONACCI SEQUENCE: "))
        if value == 1:
            sum = 1
        else:
            while (cont<value):
                result = last + next_to_last
                next_to_last,last = last,result
                cont = cont+1
            if cont == value:
                sum = next_to_last+last
        print("THE RESULT OF YOURS FIBONACCI SEQUENCE IS: {} ".format(sum))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def fat(): #FATORIAL FUNCTION
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        number = int(input("NUMBER: "))
        fat=1 
        cont=2
        while cont<=number:
            fat*=cont
            cont+=1

        print("FATORIAL RESULT: {}".format(fat))
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

def prime(): #FUNCTION FOR VERIFY IF THE NUMBER IS PRIME
    try: 
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        number = int(input("NUMBER: ")) 
        if (number == 2) or (number ==3):
            print("PRIME!")
        else:
            cont=0
            for i in range(2,number):
                if number % i == 0:
                    cont+=1
            
            if cont ==0:
                print("PRIME!")
            else:
                print("NOT A PRIME!")
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass
    
def even(): #FUNCTION FOR VERIFY IF THE NUMBER IS EVEN
    try:
        print("\n" * os.get_terminal_size().lines) #COMMAND TO CLEAN THE CONSOLE
        number = int(input("NUMBER: "))
        if number % 2 == 0:
            print("EVEN")
        else:
            print("ODD")
    except:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
        pass

    




print("PLEASE SELECT A OPERATION") 
print("---------------------------")
print("1: SUM")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")
print("5: FIBONACCI SEQUENCE")
print("6: FACTORIAL")
print("7: VERIFY IF A NUMBER IS PRIME")
print("8: VERIFY IF A NUMBER IS EVEN")

try:
    choice = int(input ("YOUR CHOICE: "))
    if choice == 1:
        sumn()
    elif choice == 2:
        sub()
    elif choice ==3:
     multi()
    elif choice == 4:
        divi()
    elif choice == 5:
        fibonnaci()
    elif choice == 6:
        fat()
    elif choice == 7:
        prime()
    elif choice == 8:
        even()
    else:
        print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
except:
    print("SORRY I DIDN'T UNDERSTAND YOUR OPTION!")
    pass








