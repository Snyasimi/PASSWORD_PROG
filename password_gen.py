import random
import string
import os

numbers = string.digits
letters = string.ascii_lowercase
upper = string.ascii_uppercase
all = numbers + letters + upper + string.punctuation
name_of_user = ""



def view_passwords(name_of_user ):
    #TODO validate the user
    """takes in the name of the user who wants to view the passwords stored 
    if the user exists it opens the folder reads the txt file contents and 
    display them on screen"""
    print("VIEWING STORED PASSWORDS......\n >Displaying...")
    list_of_dirs = os.listdirs(os.getcwd())
    if name_of_user in list_of_dirs:
        os.chdir(name_of_user)
        #To either open SAVED  or GENERATED  passwords
        view = input("To view GENERATED PASSWORDS PRESS (G) To view ADDED PASSWORDS press (A)").lower()

        if view == "a":
            with open ("pass_added.txt","r") as f:
                txtfile = f.read()
                print(txtfile)
        elif view == "g":
            with open (f"{name_of_user}.txt","r") as f:
                text_file = f.read()
                print(text_file)

        else:
            print("PLEASE PICk EITHER (G) OR (A)") 
    
    else:
        print(f"ERROR\n {name_of_user} You have no passwords saved ")
        




def add__pass(name, added_password):
    """Find the folder as the acc to save the password if non exist it will create
    Takes in a password as argument this password is writen to the file
***ACC NAME***  """
    try:


       # name = input("Whats your name?")
        # os.chdir(os.getcwd())
        dirs_in_target = os.listdir(os.getcwd())
        # print(os.getcwd())
        acc_of_password = input("THE PASSWORD BELONGS TO WHICH ACC?")
        if name in dirs_in_target:
            print("item exists")
            os.chdir(name)
            # return  True
            with open ("pass_added.txt","a") as f:
                f.write(f"You added apassword ({added_password}) for your {acc_of_password} account\n")

#TODO fix writing fuction to dispaly the appropriate message

        else:
            print("ITEAM DOES NOT EXIST\n MAKING FOLDER NOW...")
            os.mkdir(name)
            print("FOLDER MADE...")
            os.chdir(name)

            # TODO MAKE THE OS CHDIR TO THE PREVIOUS PATH AFTER WRITING THE FILE
            # return False
            with open("pass_added.txt", "a") as f:
                f.write(f"You added a password ({added_password}) for your {acc_of_password} account \n")




    except:
        print("RESTART THE PROGRAM")


def find_folder_and_make(name_of_dir):
    """Takes in name of a folder as an argument,checks if the folder exists
    .....if the folder does not exist it creates the folder and names it according
    to the given argument"""
    # os.chdir(os.getcwd())
    dirs_in_target = os.listdir(os.getcwd())
    # print(os.getcwd())
    if name_of_dir in dirs_in_target:
        print("item exists")
        os.chdir(name_of_dir)
        # return  True

    else:
        print("ITEAM DOES NOT EXIST\n MAKING FOLDER NOW")
        os.mkdir(name_of_dir)
        os.chdir(name_of_dir)

        # TODO MAKE THE OS CHDIR TO THE PREVIOUS PATH AFTER WRITING THE FILE
        # return False


def make_password():
    """This method/fuction generates a random password
    it picks random characters from the 'all' variable which consists of
    letters,numbers and symbols...the password created with this func. 
    characters will (can) be repeated"""

    psch = random.choices(all, k=user_pass_length)
    psch = "".join(psch)
    acc = input("FOR WHICH ACC")
    pass_prompt = "Password for "
    print(f"{name_of_user} your password is {psch}")
    print("PASSWORD SAVED!!")
    print("---------------------------------------------------")
    with open(f"{name_of_user}.txt", "a") as f:
        f.write(name_of_user + " " + pass_prompt + acc + " " + psch + "\n")


def unique_passwords():
    """this function generates an random pass just like the other..
    but this one selects unique characters and throughtout the password nothing is repeated"""

    p_sch = random.sample(all, k=user_pass_length)
    p_sch = "".join(p_sch)
    acc = input("FOR WHICH ACC?")
    pass_prompt = "Password for "

    print(f"{name_of_user} your password for {acc} is {p_sch}")
    print("PASSWORD SAVED !!")
    print("----------------------------------------------------")

    with open(f"{name_of_user}.txt", "a") as f:
        f.write(name_of_user + " " + pass_prompt + acc + " " + p_sch + "\n")


def validate(user_input):
    """this function takes in the user inputs and makes sure that the 
    user did not type a zero """

    #TODO validate the user  input to see if they are digits

    if user_input < 0:

        return "Please enter a number more than 0"
    


option = ""
main = input("""TO START THE PASSWORD GENERATOR PRESS (S) OR (Q) TO EXIT
__________________________________________________________________________
---------------------------------------------------------------------------\n""")
# main = input("TO EXIT THE PROGRAM PRESS Q ").lower()

main.lower()

while main != "q":
    try:
        if main != "q":

            print("""ACC AND PASSWORD WILL BE DISPLAYED AND SAVED PRESS ENTER TO CONTINUE
---------------------------------------------------------------------
PRESS (Q) TO QUIT THE PROGRAM\nTO SAVE PASSWORDS PLEASE PRESS (s)\n""")

            #HOME1 = ""
            #os.chdir()

            name_of_user = input("PLEASE ENTER YOUR NAME\n")
            if name_of_user == "q":
                break

            elif name_of_user== "s":
                name = ""
                name = input("Pleasse enter your name\n")

                pass_to_add = input("PLEASE INPUT PASSWORD TO ADD\n")
                add__pass(name,pass_to_add)

                break

            else:
                find_folder_and_make(name_of_user)

            num_of_passwords = int(input("ENTER THE AMOUNT OF PASSWORDS NEEDED:\n"))

            user_pass_length = int(input("ENTER THE LENGHT OF THE PASSWORD:\n"))

            password_type = input("FOR PASSWORD TO BE OF UNIQUE CHARACTERS PRESS (U) ELSE PRESS (C)").lower()

            if password_type == "u":
                for i in range(num_of_passwords):
                    unique_passwords()
                    

                break


            # print("please enter a number")
            elif password_type == "c":
                for i in range(num_of_passwords):
                    make_password()

                    
                
                break
            
        


            else:
                
                password_type = input("PLEASE CHOOSE BETWEEN (U) or(C)")

        
        



        elif name_of_user == "q":
            break
    
    
    except ValueError:
            
        print("please enter a digit")






