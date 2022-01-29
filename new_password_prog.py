import random
import string
import os
import smtplib
from email.message import EmailMessage


numbers = string.digits
letters = string.ascii_lowercase
upper = string.ascii_uppercase
all = numbers + letters + upper + string.punctuation

Home_dir = os.getcwd()
#TODO get email adress
#TODO validate user input to avoid breaking of program

def SendMail(msgc):
    #TODO set email and  password as env variables

    email_adress = "stevesolomon1229"
    epassword = ""
    msg=EmailMessage()
    msg["Subject"] = "REQUESTED PASSWORDS"
    msg["From"] = email_adress
    msg["To"] = EMAIL_ADRESS
    msg.set_content(msgc)


    with smtplib.SMTP_SSL("smtp.gmail.com","465") as smtp:
        smtp.login(email_adress,epassword)
        smtp.send(msg)

def sendPassword(name):
    """takes the name dir and file type and sends it to a specified email
    given buy the user """
    #TODO add feature to send specific passwords for specific accounts

    #EmailAdress = input("Which email would you like the passwords to be sent to?\n")

    GenOrSaved = input("Which passwords would you like to send,Generated or Saved..\nPlease select (G) or (S)\n").lower()
    
    #OPEN FILES AND DIRS FOR THE PASSWORD
    
    if name in Home_dir:
        os.chdir(name)
        if GenOrSaved == "g":
            with open(f"{name}.txt","r") as f:

                contents = f.read()
            return contents
        elif GenOrSaved == "s":
            with open ("pass_added.txt","r")as f:

                contents = f.read()
            return contents
        else :
            print("please choose either G or S\n....Restarting....\n")
    else:
        print(f"{name} You have no passwords saved")





def view_passwords(name):
    try:

    #TODO validate the user
        """takes in the name of the user who wants to view the passwords stored 
        if the user exists it opens the folder reads the txt file contents and 
        display them on screen"""
        print("VIEWING STORED PASSWORDS......\n >Displaying...")
        list_of_dirs = os.listdir(os.getcwd())
        if name in list_of_dirs:
            os.chdir(name)
            #To either open SAVED  or GENERATED  passwords
            view = input("To view GENERATED PASSWORDS PRESS (G) To view ADDED PASSWORDS press (A)").lower()

            if view == "a":
                with open ("pass_added.txt","r") as f:
                    txtfile = f.read()
                    print(txtfile)
            elif view == "g":
                with open (f"{name}.txt","r") as f:
                    text_file = f.read()
                    print(text_file)

            else:
                print("PLEASE PICk EITHER (G) OR (A)") 
    
        else:
            print(f"ERROR\n {name} You have no passwords saved ")
    except FileNotFoundError:
        print("ERROR>>>>\n....You have no such  passwords")




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
                os.chdir(Home_dir)
#TODO fix writing fuction to dispaly the appropriate message

        else:
            pass
            #print("ITEAM DOES NOT EXIST\n MAKING FOLDER NOW...")
            #os.mkdir(name)
            #print("FOLDER MADE...")
            #os.chdir(name)

            # TODO MAKE THE OS CHDIR TO THE PREVIOUS PATH AFTER WRITING THE FILE
            # return False
            with open("pass_added.txt", "a") as f:
                f.write(f"You added a password ({added_password}) for your {acc_of_password} account \n")
                os.chdir(Home_dir)



    except:
        print("RESTART THE PROGRAM")


def find_folder_and_make(name):
    """Takes in name of a folder as an argument,checks if the folder exists
    .....if the folder does not exist it creates the folder and names it according
    to the given argument"""
    # os.chdir(os.getcwd())
    dirs_in_target = os.listdir(os.getcwd())
    # print(os.getcwd())
    if name in dirs_in_target:
        print("item exists")
        os.chdir(name)
        # return  True

    else:
        print("ITEAM DOES NOT EXIST\n MAKING FOLDER NOW")
        os.mkdir(name)
        os.chdir(name)

        # TODO MAKE THE OS CHDIR TO THE PREVIOUS PATH AFTER WRITING THE FILE
        # return False


def make_password():
    """This method/fuction generates a random password
    it picks random characters from the 'all' variable which consists of
    letters,numbers and symbols...the password created with this func. 
    characters will (can) be repeated"""

    psch = random.choices(all, k=USER_PASS_LENGHT)
    psch = "".join(psch)
    acc = input("FOR WHICH ACC")
    pass_prompt = "Password for "
    print(f"{name} your password is {psch}")
    print("PASSWORD SAVED!!")
    print("---------------------------------------------------")
    with open(f"{name}.txt", "a") as f:
        f.write(name + " " + pass_prompt + acc + " is "+  psch + "\n")
        #os.chdir(Home_dir)


def unique_passwords():
    """this function generates an random pass just like the other..
    but this one selects unique characters and throughtout the password nothing is repeated"""

    p_sch = random.sample(all, k=USER_PASS_LENGTH)
    p_sch = "".join(p_sch)
    acc = input("FOR WHICH ACC?")
    pass_prompt = "Password for "

    print(f"{name} your password for {acc} is {p_sch}")
    print("PASSWORD SAVED !!")
    print("----------------------------------------------------")

    with open(f"{name}.txt", "a") as f:
        f.write(name + " " + pass_prompt + acc + " is " + p_sch + "\n")
        #os.chdir(Home_dir)


def validate(user_input):
    """this function takes in the user inputs and makes sure that the 
    user did not type a zero """

    #TODO validate the user  input to see if they are digits

    if user_input < 0:

        return "Please enter a number more than 0"
    





print("PASSWORD PROG>>>>>\n")

prompt = input("HELLO USER PLEASE ENTER ANY VALUE FOR OPTION\n....PRESS Q TO QUIT\n").lower()
while prompt != "q":
    name = input("PLEASE STATE YOUR NAME\n")

    input_option = input("PRESS (A) TO ADD PASSWORD\nPRESS (V) TO VIEW PASSWORDS\nPRESS (G) TO GENERATE PASSWORDS\nPRESS (S) TO SAVE PASSWORDS\n PRESS (SM) TO SEND SAVED PASSWORDS TO YOUR EMAIL\nPRESS (Q) TO QUIT PROGRAM\n").lower()

    #name = print("PLEASE ENTER YOUR NAME\n")
    



    if input_option == "a":
        find_folder_and_make(name)

        NO_OF_ADDED_PASSWD = int(input("How many passwords would you like to save?\n"))
    


        for passw in range(NO_OF_ADDED_PASSWD):

            added_password = input("Which password would you like to add or save\n")
    
            add__pass(name,added_password)
            print("Password added.....\n")
            os.chdir(Home_dir)


    elif input_option =="v":
        
        
        view_passwords(name)
        os.chdir(Home_dir)

    elif input_option == "g":
        find_folder_and_make(name)

        number_of_passwords = input("How many passwords do you need?\n")

        USER_PASS_LENGTH = int(input("How long would you like the passwords to be?\n"))

        type_of_password = input("If you wish for the characters  of the password to be unique please press (U)..else some characters will be REPEATED\n")
        try:
            for i in range(int(number_of_passwords)):
                if type_of_password == "u":
                    unique_passwords()
                    #os.chdir(Home_dir)

                else:
                    make_password()
                    #os.chdir(Home_dir)

            os.chdir(Home_dir)

        except ValueError:
            print("PLEASE ENTER THE SPECIFIED INPUTS")

    
    elif input_option == "sm":
        EMAIL_ADRESS = input("Enter Your Email Adress\n ")

        SendMail(sendPassword(name))
        print("Sending Email....\nPlease wait")
        os.chdir(Home_dir)

    elif input_option == "q":
        break






