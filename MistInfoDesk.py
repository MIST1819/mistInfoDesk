import os
import time
import json
import sys
import pyfiglet

os.system('cls')

ascii_banner = pyfiglet.figlet_format("We are MIST!!")
for l in ascii_banner:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)

text1 = "Welcome to MIST registration portal!! \n \n"
for l in text1:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)

# name
name = input("What is your name?: ")
print("\n")
time.sleep(1)
os.system('cls')
name_banner = pyfiglet.figlet_format(name)
print(name_banner)
time.sleep(1)
os.system('cls')

# email
print(name_banner)
print("\n")
email = input("Tell us your email: ")
print("\n")
time.sleep(1)
os.system('cls')
print(name_banner)
print("\n")
print("Recorded email:  " + email)
time.sleep(1)
os.system('cls')

# phone number
print(name_banner)
print("\n")
phoneNo = input("Your phone number : ")
print("\n")
time.sleep(1)
os.system('cls')
print(name_banner)
print("\n")
print("Recorded phone  +91" + phoneNo)
time.sleep(1)
os.system('cls')

# registration number
print(name_banner)
print("\n")
regNo = input("Your registration number : ")
print("\n")
time.sleep(1)
os.system('cls')
print(name_banner)
print("\n")
print("Recorded registration number " + regNo)
time.sleep(1)
os.system('cls')

# branch
print(name_banner)
print("\n")
branch = input("Branch : ")
print("\n")
time.sleep(1)
os.system('cls')
print(name_banner)
print("\n")
print("Recorded branch " + branch)
time.sleep(1)
os.system('cls')

print(name_banner)
print("\n")
wait_message = "Redirecting to confirmation page..."
for l in wait_message:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
os.system('cls')

recorder_Info = "All your responses were recorded successfully.\n But they are not saved yet.\n Verify your entry by typing yes"
for l in recorder_Info:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.09)
print("\n")
print(name_banner)
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
if confirmMess == "yes" or confirmMess == "Yes":
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
elif confirmMess == "no":
    print("Alright. We are redirecting you to the form again. This time, don't make an error.")
    os.system('cls')
    os.system('python MistInfoDesk.py')
else:
    print("Errors are the root of all evil and this is what you just did. Now refill the form")

time.sleep(5)
os.system('cls')
reStart = input("Use mancomm code to quit, else type anything else:  ")
if reStart == 3000:
    print("The commmand ends now")
else:
    os.system('MistInfoDesk.py')
