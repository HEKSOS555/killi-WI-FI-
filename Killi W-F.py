import os
os.system ("clear")
import random
import getpass


print("×===========×===========×")
print("      killi WI-FI ")
print("×===========×===========×")
print("  YouTube : MR.HEKSOS ")
print("×===========×===========×")
print("")
password = input ('Enter password : ')
#determine if the password is correct
if password == "H01":
	print(" >>>>[H01]<<<<")
wifi = input ('Enter name Wi-Fi : ')
print("")
print("")

def GetPassword(data):
	Max = 8
	password=""
	while len(password) != Max:
		value = random.choice(data)
		password += value
	return password

data ='123456789poiuytrewqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$-&.*0":?!)/&'
for i in range (20):
	print(GetPassword(data))

print("")
print("")
print("=================")
print("  py_HEKSOS")
print("=================")
print("")