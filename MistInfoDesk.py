import os
import time
import json

os.system('cls')


# name
name = input("What is your name?: ")
print("\n")
print("Hello " + name)
print("\n")
# email
email = input("Tell us your Email Address: ")
print("\n")
print("Recorded email  " + email, "red")
print("\n")
# phone number
phoneNo = input("Your phone number : ")
print("\n")
print("Recorded phone  +91" + phoneNo)
print("\n")
# registration number
regNo = input("Your registration number : ")
print("\n")
print("Recorded registration number " + regNo)
print("\n")
# branch
branch = input("Branch : ")
print("\n")
print("Recorded branch " + branch)
print("\n")
time.sleep(1)
os.system('cls')
print("Redirecting to confirmation page...")
time.sleep(2)
os.system('cls')

print("All your responses were recorded successfully.\n But they are not saved yet.\n Verify your entry by typing yes")
print("\n")
print("\n")
print("Name: " + name + "\n")
print("Email: " + email + "\n")
print("Phone: +91" + phoneNo + "\n")
print("Reg. No.: " + regNo + "\n")
print("Branch: " + branch + "\n")
print("\n")
print("\n")
confirmMess = input("Is this correct? Typy 'Yes' or 'No': ")
if(confirmMess == "yes" or confirmMess == "Yes"):
    os.system('cls')
    print("Good. Your messages were recorded. It's been saved on our system. See you in the recruitments.")
    deskCode = {
        "name": name,
        "email": email,
        "phone": phoneNo,
        "regno": regNo,
        "branch": branch
    }
    with open("./responses/" + regNo + ".json", "w") as json_file:
        json.dump(deskCode, json_file)
elif (confirmMess == "no"):
    print("Alright. We are redirecting you to the form again. This time, don't make an error.")
    os.system('cls')
    os.system('python MistInfoDesk.py')

time.sleep(3)
os.system('cls')
os.system('MistInfoDesk.py')
