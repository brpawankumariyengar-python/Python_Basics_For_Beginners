#The program attempts to find out all prime numbers

import math

def Pawan_Prime_Number_Locator(Number_Input,Options):
	Options = Options.upper()
	try:
		X = int(Number_Input)
		if X == 5 or X == 7 or X ==3:
			print("Congratulations! The number "+str(X)+" is a prime number. Well done")
			if Options == 'ALL' or Options == 'PRIME':
				return {X:"Prime Number"}
		else:
			if X == 1:
				print("The number one(1)is unity and is neither prime nor composite")
				if Options == 'ALL':
					return {X:"Unity"}
			elif X == 2:
				print("Congratulations! The number "+str(X)+" is a prime number. Well done")
				if Options == 'ALL' or Options == 'PRIME':
					return {X:"Prime Number"}
			elif X > 2:
				if X % 2 == 0:
					print("Sorry to report that the number  "+str(X)+" is not a prime number. Better luck next time")
					if Options ==  'ALL' or Options == 'COMPOSITE':
						return {X:"Composite Number"}
				else:
					Y = math.floor(math.sqrt(X))
					for Ctr in range(3,Y+1,2):
						if X % Ctr == 0:
							Check_Prime = False
							break
						else:
							Check_Prime = True
					if Check_Prime == True:
						print("Congratulations! The number "+str(X)+" is a prime number. Well done")
						if Options == 'ALL' or Options == 'PRIME':
							return {X:"Prime Number"}
					else:
						print("Sorry to report that the number  "+str(X)+" is not a prime number. Better luck next time")
						if Options ==  'ALL' or Options == 'COMPOSITE':
							return {X:"Composite Number"}
			else:
				print("Invalid input. Kindly enter a number greater than one (1)")
		
	except OSError as err:
		print("OS error: {0}".format(err))
	except ValueError:
		print("Invalid input. Please enter a number greater than one(1) in digits")
	except:
		print("Unexpected error:")
		raise 



if __name__ == '__main__':
	X = input("Enter a number to know if it is a prime number or not:  ")
	Pawan_Prime_Number_Locator(X)
