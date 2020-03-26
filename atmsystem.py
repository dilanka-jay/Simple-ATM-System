#---------simplle ATM system--------


#verify user pin code
#1234 is the valid pin code for the user
def verify_key(pin):
	if pin == "1234":
		return True
	else:
		return False
		
#login function for the system		
def log_in():
	tries = 0
	while tries<4:
		pin = input("Enter a pin number: ")
		
		if verify_key(pin):
			print("\nPin number accepted!")
			return True
		else:
			print("Invalid pin number!")
			tries+=1
			
	print("Too many incorrect tries. Access denied!")
		 
#main part of the simple atm system		
def main():

		print("===== Welcome to  simple atm system =====\n\n")
		
		#user's account information
		balance = 1000.00
		acc_no = 22358
		
		if log_in():
			print("\npress 1 to check your account" )
			print("press 2 to deposit")
			print("press 3 to draw")
		
			while True:
			    option = print("\nEnter your choice : ")
			    option = input()
				
				#checking user's choices
			    if option == "1":
				    print("\nYour current balance is : Rs.", balance)
				    print("Your account number is: ", acc_no)
				    exit=input("\nDo you want to exit? (yes/no) : ")
				    if exit.lower() in("yes","y"):
				      print("Thank you!")
				      break
				    	
			
			    elif option == "2":
			    	deposit = float(input("How much do you want to deposit? : "))
			    	balance = balance+deposit
			    	print("Your current balance is: Rs.", balance)
			    	exit = input("\nDo you want to exit? (yes/no) : ")
			    	if exit.lower()in ("yes" , "y"):
			    		print("Thank you!")
			    		break
			    	
			    	
			    elif option == "3":
			    	draw = float(input("How much do you want to draw? : "))
			    	if balance>draw:
			    		balance = balance-draw
			    		print("Your current balance is: Rs.", balance)
			    		exit = input("\nDo you want to exit? (yes/no) : ")
			    		if exit.lower()in ("yes","y"):
			    			print("Thank you")
			    			break
			    	else:
			    		print("Invalid amount!")
			    		exit = input("\nDo you want to exit? (yes/no) :")
			    		if exit.lower()in ("yes","y"):
			    			print("Thank you!")
			    			break
			    		
			    else :
			    	print("Please make a choice!.(1),(2) or(3)")
			    

				
main()	
	