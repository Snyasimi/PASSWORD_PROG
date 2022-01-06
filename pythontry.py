
import random
import string
numbers = string.digits
letters = string.ascii_lowercase
upper = string.ascii_uppercase
all = numbers + letters +upper


def make_password():
    psch = random.choices(all, k=user_pass_length)
    psch = "".join(psch)
    acc = input("FOR WHICH ACC")
    print(f"{name_of_user} your password is {psch}")
    print(f"{name_of_user} your password for {acc} " is {p_sch}")"
    #with open ("pass.txt","a") as f:
       # f.write(psch +"\n")



def unique_passwords():
    p_sch = random.sample(all,k=user_pass_length)
    p_sch = "".join(p_sch)
    acc = input ("FOR WHICH ACC?")
    print(f"{name_of_user} your password for {acc} "is {p_sch}")
    #with open ("pass.txt","a") as f:
         # f.write(p_sch +"\n")

def validate():
    if user_pass_length and num_of_passwords <0:
        print("please enter a number more than 0")



main = input("TO Sart the program please press (s) or (q) to exit")
main.lower()
while main != "q":
    try:


        user_pass_length = int(input("ENTER THE LENGHT OF THE PASSWORD:\n"))

        name_of_user = input("PLEASE ENTER YOUR NAME")
        num_of_passwords = int(input("ENTER THE AMOUNT OF PASSWORDS NEEDED:\n"))

        password_type = input("FOR PASSWORD TO BE OF UNIQUE CHARACTERS PRESS (U) ELSE PRESS (C)").lower()

        if password_type == "u":
            for i in range(num_of_passwords):

                unique_passwords()



       # print("please enter a number")
        elif password_type == "c":
            for i in range(num_of_passwords):
                make_password()

        else:
            password_type = input("PLEASE CHOOSE BETWEEN (U) or(C)")
            continue


    except ValueError:
        print("please enter a digit")


