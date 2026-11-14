import hashlib
import sys

def enter_password(Puser_pass): # function asking for user to enter pass
    while True:
        password = input("Enter a password: ")
        if password.strip() == "": # presence check
            print("Password can not be empty.")

        elif len(password) < 3: # length check
            print("Password must be over 3 characters long.")
        else:
            print(password)
            return password

def check_plaintext_pass(Puser_pass):
    passwords = open("passwords.txt", "r", encoding="utf8", errors="ignore") # prevent unicode error
    for password in passwords: 
        password = password.strip() # removing leading spaces
        if password == Puser_pass:
            print("your password is found on a public database.")
            return True

    print("your password is not found!")
    return False
        
def check_hashed_pass(Puser_pass):
    hashed_password = hashlib.sha1(Puser_pass.encode()).hexdigest() # turn to bits, then hash code then hash

    passwords = open("passwords_SHA1.txt", "r", encoding="utf8", errors="ignore") # ignoring unrecognised characters
    for password in passwords: # looping over passwords
        password = password.strip()
        if password == hashed_password:
            print("your password is found on a public database.")
            passwords.close()
            return True

    print("Your password is not found")
    passwords.close()
    return False

def user_interface():
    user_pass = ""
    weakpass = False

    while True:
        print("Hello! this is xCrckr password cracker and we're going to check if your password is common or not!\nThis works through using a list of well known passwords and matching your pasword against it.\nAnd you'll be pleased to know that there's a choice to check against hashed passwords too! (SHA-1)\n(The file used as a passwords.txt basis is RockYou.txt by the way.)")
        while True:
            while True:
                print("Type 1 to check a plaintext password")
                print("Type 2 to check a hashed password")
                print("press ENTER to leave")

                choice = input()
                if choice == "":
                        print("thank you for using my script!")
                        sys.exit(0)

                if choice == "1":
                    user_pass = enter_password(user_pass)
                    weakpass = check_plaintext_pass(user_pass)

                elif choice == "2":
                    user_pass = enter_password(user_pass)
                    weakpass = check_hashed_pass(user_pass)
            
                else:
                    print("please enter a valid option.")


user_interface()
