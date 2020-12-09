import pickle
from datetime import datetime
import pytz
from os import system, name 
from time import sleep 
def clear(): 
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')

def login():
	filename='users'
	f=open(filename,'rb')
	users_dict=pickle.load(f)
	f.close()
	username=input("Enter Username : ")
	password=input("Enter Password : ")
	if(username in users_dict.keys()):
		if(password==users_dict[username]):
			print("Login Success")
			ret=[True,username,password]
			return ret
		else:
			print("Incorrect password")
			return False
	else:
		print("Username doesn't exist")
		return False

def signup():
	filename='users'
	f=open(filename,'rb')
	users_dict=pickle.load(f)
	f.close()
	username=input("Enter New username : ")
	password=input("Enter Password : ")
	if(username in users_dict.keys()):
		print("Username already exists, Pick another Username or Try logging in")
		return False
	else:
		users_dict[username]=password
		f=open(filename,'wb')
		pickle.dump(users_dict,f)
		f.close()
		print("User Created Successfully")
		return True

def update_profile():
	filename='users'
	f=open(filename,'rb')
	users_dict=pickle.load(f)
	f.close()
	print("Please Login again to change your username info")
	ret=login()
	if(ret[0]==True):
		new_username=input("Enter the Updated username")
		del users_dict[ret[1]]
		users_dict[new_username]=ret[2]
		f=open(filename,'wb')
		pickle.dump(users_dict,f)
		f.close()
		print("Username Updated succesfully")

def change_password():
	filename='users'
	f=open(filename,'rb')
	users_dict=pickle.load(f)
	f.close()
	print("Please Login again to change your password")
	ret=login()
	if(ret[0]==True):
		new_password=input("Enter Updated password")
		del users_dict[ret[1]]
		users_dict[ret[1]]=new_password
		f=open(filename,'wb')
		pickle.dump(users_dict,f)
		f.close()
		print("Password Updated succesfully")

def reserve_ticket(username):
	filename="tlist"
	f=open(filename,'rb')
	tlist=pickle.load(f)
	f.close()
	x=1
	for i in tlist:
		print(x,".) ",i)
		x=x+1
	trainNo=int(input("Enter the Serial number of the Train you want to book Ticket in :"))-1
	res=open("Reservations.txt","a")
	tz=pytz.timezone('Asia/Kolkata')
	quota=input("Which quota do you want to reserve your ticket in(GN/TK/EM): ")
	res_string=username+" booked a ticket in train no "+tlist[trainNo]+" in "+quota+" quota "+str(datetime.now(tz))+"\n"
	res.write(res_string)
	res.close()
	print("Seat booked Successfully")

def add_train(username):
	filename="admin"
	f=open(filename,'rb')
	admin=pickle.load(f)
	f.close()
	filename="tlist"
	f=open(filename,'rb')
	tlist=pickle.load(f)
	f.close()
	if(username in admin):
		new_item=input("Enter The Train Number to be added : ")
		tlist.append(new_item)
		f=open(filename,'wb')
		pickle.dump(tlist,f)
		f.close()
	else:
		print("User not in Admin list. Access Denied.")

counter=True
while(counter):
	clear()
	print("\nWelcome to Food ordering System :")
	print("1.Login\n2.Signup\n3.Exit")
	ch=int(input("Enter your choice : "))
	if(ch==1):
		counter2=True
		ret=login()
		sleep(1)
		while(counter2):
			sleep(1)
			clear()
			print("1.Reserve A Ticket\n2.Add train(Admin only)\n3.Update Profile\n4.Change Password\n5.Logout")
			ch2=int(input("Enter your choice : "))
			if(ch2==1):
				reserve_ticket(ret[1])
			elif(ch2==2):
				add_train(ret[1])
			elif(ch2==3):
				update_profile()
			elif(ch2==4):
				change_password()
			else:
				counter2=False

	elif(ch==2):
		signup()
	else:
		counter=False