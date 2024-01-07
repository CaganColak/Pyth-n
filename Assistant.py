import datetime
import time
import random




an = datetime.datetime.now()
tarih = datetime.datetime.ctime(an)
liste = []
rehber = {}
print("Special ASSISTANT")
print("Codded By Cagan")
while True:

    command = input("Command ['help' for help]: ")
    
    
    if command == "help":
        print("calculator : opens a basic calculator.")
        print("date : shows the date")
        print("list : opens a list")
        print("show_list : shows the list")
        print("search_list : searchs a name in the list")
        print("add_to_list : adds something to the list")
        print("delete_from_list : deletes something from the list")
        print("contacts : shows the contacts")
        print("add_contact : adds a contact")
        print("search_contact : searchs a contact")
        print("delete_contact : deletes a contact")
        print("random_number : generates a random number")
        print("password_generator : generates a random password")
        
    elif command == "calculator":
        a = int(input("number one:"))
        b = int(input("number two:"))
        c = input("operation(addition, subtraction, multiplication, division):")
        
        if c == "addition":
            print(a+b)
        if c == "subtraction":
            print(a-b)
        if c == "multiplication":
            print(a*b)
        if c == "division":
            print(a/b)
            
    elif command == "date":
        print(an)
        print("--------------------------")
        print(tarih)
        
    elif command == "list":
        print(liste)
        
    elif command == "show_list":
        print(liste)
        
    elif command == "search_list":
        search = input("search something:")
        if search in liste:
            print("found!")
            
    elif command == "add_to_list":
        add2 = input("add something:")
        liste.append(add2)
        
    elif command == "delete_from_list":
        delete = input("name:")
        if delete in liste:
            liste.remove(delete)
        else:
            print("no contents found.")
            
    elif command == "contacts":
        print(rehber)
        
    elif command == "add_contact":
        name = input("name:")
        number = int(input("number"))
        rehber[name] = number
        
    elif command == "search_contact":
        letter = input("initial:")
        for k in rehber.keys():
            if k[0] == letter:
                print(k, ":", rehber[k])
            else:
                print("no contents found")
    
    elif command == "delete_contact":
        delete2 = input("name:")
        if delete2 in rehber:
            del rehber[delete2]
            
    elif command == "random_number":
        randomnumber = int(input("number range(small number):"))
        randomnumber2 = int(input("number range(big number):"))
        r_n = random.randint(randomnumber, randomnumber2)
        print("generated number:",r_n)
        
    elif command == "password_generator":
        digits = int(input("number of digits (4, 8):"))
        if digits == 4:
            digit4 = random.randint(1000, 10000)
            print("generated password:", digit4)
        elif digits == 8:
            digit8 = random.randint(10000000, 100000000)
            print("generated password:", digit8)
        else:
            print("no digit like this.")