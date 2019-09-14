import os
import time
import json
import sys
import pyfiglet
import signal
import random

os.system('clear')
x = 0
numCat = 0

while x < 20000:
    randNum = random.randint(0, 1)
    numCat = str(numCat) + ' ' + str(randNum) + ' '
    x = x + 1

for l in numCat:
    sys.stdout.write(l)
    sys.stdout.flush()

time.sleep(2)
os.system("clear")

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
os.system('clear')
name_banner = pyfiglet.figlet_format(name.split()[0])
print(name_banner)
time.sleep(1)
os.system('clear')

# email
print(name_banner)
print("\n")
email = input("Tell us your email: ")
print("\n")
time.sleep(1)
os.system('clear')
print(name_banner)
print("\n")
print("Recorded email:  " + email)
time.sleep(1)
os.system('clear')

# phone number
print(name_banner)
print("\n")
phoneNo = input("Your phone number : ")
print("\n")
time.sleep(1)
os.system('clear')
print(name_banner)
print("\n")
print("Recorded phone  +91" + phoneNo)
time.sleep(1)
os.system('clear')

# registration number
print(name_banner)
print("\n")
regNo = input("Your registration number : ")
print("\n")
time.sleep(1)
os.system('clear')
print(name_banner)
print("\n")
print("Recorded registration number " + regNo)
time.sleep(1)
os.system('clear')

# redirection page
print(name_banner)
print("\n")
wait_message = "Redirecting to confirmation page..."
for l in wait_message:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
os.system('clear')

# verification page
verification_Banner = pyfiglet.figlet_format("Verify")
print(verification_Banner)
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
print("\n")
print("\n")
confirmMess = input("Is this correct? Type 'Yes' or 'No': ")
if confirmMess == "yes" or confirmMess == "Yes":
    os.system('clear')
    print("Good. Your messages were recorded. It's been saved on our system. See you in the recruitments.")
    deskCode = {
        "name": name,
        "email": email,
        "phone": phoneNo,
        "regno": regNo
    }
    with open("./responses/" + regNo + ".json", "w") as json_file:
        json.dump(deskCode, json_file)
elif confirmMess == "no":
    print("Alright. We are redirecting you to the form again. This time, don't make an error.")
    os.system('clear')
    os.system('python MistInfoDesk.py')
else:
    print("Errors are the root of all evil and this is what you just did. Now refill the form")

time.sleep(5)
os.system('clear')
os.system('MistInfoDesk.py')
