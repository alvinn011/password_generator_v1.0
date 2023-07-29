import random
import hashlib
print ("""
                                            _                                   _ 
                                           | |                                 | |            
  _ __   __ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_) | (_| \__ \__ \\  V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 | |                                             __/ |                               [v1.0]         
 |_|                                            |___/                        [By Alvinn011]                        
""")  
while True :  
    print ("""
    choose your password lenght:
    1) ~20 characters
    2) ~64 characters
    3) ~96 characters
    4) ~128 characters
    5) ~375 characters  (X_X)
    """)
    answer = input("- ")

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "()[]{}+*#!$"
    all = lower + upper + numbers + symbols
    password1 = "".join(random.sample(all,4)) + "-" 
    password2 = "".join(random.sample(all,4)) + "-" 
    password3 = "".join(random.sample(all,4)) + "-"
    password4 = "".join(random.sample(all,4)) 
    password = password1+password2+password3+password4
    #password ^
    word_file = "words.txt"
    WORDS = open(word_file).read().splitlines()
    password5 = "".join(random.sample(WORDS,12))
    password6 = password + "-" + password5
    #password6 ^
    hash_object = hashlib.sha256(bytes(password6,'utf-8'))
    hex_dig = hash_object.hexdigest()
    #hex_dig ^
    hash_object2 = hashlib.sha384(bytes(hex_dig,'utf-8'))
    hex_dig2 = hash_object2.hexdigest()
    #hex_dig2 ^
    wow = password +"-"+ password6 +"-"+ hex_dig +"-"+ hex_dig2
    hash_object3 = hashlib.sha512(bytes(wow,'utf-8'))
    hex_dig3 = hash_object3.hexdigest()
    #hex_dig3 ^
    wowwww = hex_dig3 + "-" + hex_dig2 + "-" + hex_dig + "-" + password6 
    #wowww ^
    
    if answer ==  "1":
        print("here is your password:")
        print(password)
        ans = input("want another password? (y/n) ")
        if ans == "y":
            pass
        if ans == "n":
            break
        else:
            if ans != "y" and ans != "n":
                print("you wrote an invalid command QUITTING!")
                break
    elif answer == "2":
        print("here is your password:")
        print(hex_dig)
        ans = input("want another password? (y/n) ")
        if ans == "y":
            pass
        if ans == "n":
            break
        else:
            if ans != "y" and ans != "n":
                print("you wrote an invalid command QUITTING!")
                break
    elif answer == "3":
        print("here is your password:")
        print(hex_dig2)
        ans = input("want another password? (y/n) ")
        if ans == "y":
            pass
        if ans == "n":
            break
        else:
            if ans != "y" and ans != "n":
                print("you wrote an invalid command QUITTING!")
                break
    elif answer == "4":
        print("here is your password:")
        print(hex_dig3)
        ans = input("want another password? (y/n) ")
        if ans == "y":
            pass
        if ans == "n":
            break
        else:
            if ans != "y" and ans != "n":
                print("you wrote an invalid command QUITTING!")
                break
    elif answer == "5":
        print("here is your password:")
        print(wowwww)
        ans = input("want another password? (y/n) ")
        if ans == "y":
            pass
        if ans == "n":
            break
        else:
            if ans != "y" and ans != "n":
                print("you wrote an invalid command QUITTING!")
                break
    else:
        print("you wrote an invalid command retry")

