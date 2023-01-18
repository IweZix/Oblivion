import random
from pystyle import *

System.Title('GenPassword')

banner = """
████▄ ███   █    ▄█     ▄   ▄█ ████▄    ▄   
█   █ █  █  █    ██      █  ██ █   █     █  
█   █ █ ▀ ▄ █    ██ █     █ ██ █   █ ██   █ 
▀████ █  ▄▀ ███▄ ▐█  █    █ ▐█ ▀████ █ █  █ 
      ███       ▀ ▐   █  █   ▐       █  █ █ 
                       █▐            █   ██ 
                       ▐                    
"""
print(Colorate.Vertical(Colors.blue_to_cyan, banner))

print(Col.blue + "For which account do you want to create a password ?")
account = input("Account : ")

print(
    Col.blue + "[1] - Basic password : 10 characters, upper and lower cases and numbers\n" +
               "[2] - Secure Password : More than 8 characters containing upper and lower case letters, with numbers and special characters")
choice = input("Choose option : ")

while choice != "1" and choice != "2":
    print(Col.red + "Invalid option !")
    choice = input(Col.red + "Choose option : ")

def BasicPassword():
    chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    password = ''

    for i in range(8):
        password = f"{password}{random.choice(chars)}"

    print(f"Password : {password}")

    with open("password.txt", "a+") as file:
        file.write(f"{account} password : {password}\n")
        file.close()

    print("\nYour password is stored in the file password.txt")

def SecurePassword():
    chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,?;.:/!§%#@"

    password = ''

    for i in range(16):
        password = f"{password}{random.choice(chars)}"

    print(f"Password : {password}")

    with open("password.txt", "a+") as file:
        file.write(f"{account} password : {password}\n")
        file.close()

    print("\nYour password is stored in the file password.txt")

if choice == '1':
    BasicPassword()

if choice == '2':
    SecurePassword()