# This python script is here to learn the sets in Python

# Sets are used when the elements are unique and order of elements is not important

Empty__Set ={}

Sample__Set__1 = {"Dexter", "Honey", "Food", "Water", "Air", "Fire", "Shelter", "Laboratory", "Secret"} #Set can contain strings

Sample__Set__2 = {1,2,3,4,5,6,7,8,9,0} # Set can contain Integer

Sample__Set__3 = {0.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0} # Set can contain float 

Sample__Set__Mixed = {"Delhi","Corona", 786, 3.14285714, 1.16, "Bad", 214, False} # Set can contain mixed Values

print("Empty set    ",Empty__Set) # Prints out the empty set {}
print()
print("Sample Set Mixed     ",Sample__Set__Mixed,"\n")



print("Attributes and functions related to sets are as:    \n", dir(set),"\n")



def Add__Element__To__Set(Pawan__Set, Element): # This function adds a provided element to the set and uses add function to add the element
	Maro_Element = Element
	if Maro_Element == "" or Maro_Element == None:
		print("No proper element was recieved in the input")
	else:
		Pawan__Set.add(Maro_Element)
		return Pawan__Set

def Remove__Known__Element__From__Set(Pawan__Set, Element): #This function removes an element from the set and uses remove function. This throws an error if element is not present in the set
	Maro_Element = Element
	Pawan__Final__Set = Pawan__Set.remove(Maro_Element)
	print("Element  "+str(Maro_Element)+"   removed successfully")
	return Pawan__Final__Set

def Remove__Probable__Element__From__Set(Pawan__Set, Element): #This function removes an element from the set and uses discard function. This does not throw an error if element is not present in the set
	Maro_Element = Element
	Pawan__Final__Set = Pawan__Set.discard(Maro_Element)
	print("Element  "+str(Maro_Element)+"   removed successfully")
	return Pawan__Final__Set


Sample__Set__A = {'Cat', 'Bat', 'Mat', 'Rat', 'Fat', 'Eat', 'Hat', 'Pat', 'Sat'}
Sample__Set__B = {'Dog', 'Cow', 'Goat', 'Rat', 'Cat', 'Bat', 'Elephant', 'Monkey', 'Tiger', 'Lion', 'Horse', 'Donkey'}

#We will show the union of the sets... this means unique elements present in one set but not in other will be added to that.
def Set_Union(set1, set2):
	A = set1
	B = set2
	Sample__Set__Union = A|B
	print(A)
	print(B)
	print(Sample__Set__Union,"  This is sample of A union B")

def Set_Intersection(set1, set2):
	A = set1
	B = set2
	Sample__Set__Intersection = A&B
	print(Sample__Set__Intersection, "   This is a sample of A intersction B")

if __name__ == "__main__":
	print("We will add an element 'Crime Master Gogo' , to our set")
	print("Sample set 1:   ",Sample__Set__1)
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Crime Master Gogo")
	print("Final result is:   ", Our__Result)
	print("Sammple set 2   ", Sample__Set__2)
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Crime Master Gogo")
	print("Final result is:   ", Our__Result)
	print("\n")


	print("We will now remove Crime Master Gogo from our  set using remove function  ")
	print("Please note that remove function returns an error if the element to be removed is not in the set")
	print("Samle set 1 is   ", Sample__Set__1)
	print("Samle set 2 is   ", Sample__Set__2)
	print("Now let us use remove function")
	Sample__Set__1.remove("Crime Master Gogo")
	Sample__Set__2.remove("Crime Master Gogo")
	print("Samle set 1 is   ", Sample__Set__1)
	print("Samle set 2 is   ", Sample__Set__2)
	print("\n")


	Our__Result = Add__Element__To__Set(Sample__Set__1,"Crime Master Gogo")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Crime Master Gogo")
	print("We will now remove Crime Master Gogo from our  set using discard function  ")
	print("Please note that discard function does notreturn an error if the element to be removed is not in the set")
	print("Samle set 1 is   ", Sample__Set__1)
	print("Samle set 2 is   ", Sample__Set__2)
	print("Now let us use remove function")
	Sample__Set__1.discard("Crime Master Gogo")
	Sample__Set__2.discard("Slime Mister Pogo")
	print("Samle set 1 is   ", Sample__Set__1)
	print("Samle set 2 is   ", Sample__Set__2)
	print("\n")


	print("Sample Set 1", Sample__Set__1)
	print("sample set 2", Sample__Set__2)
	Set_Union(Sample__Set__1,Sample__Set__2)
	print("\n")

	Our__Result = Add__Element__To__Set(Sample__Set__1,"Crime Master Gogo")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Dunder")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Lacross")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Dunder")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Lacross")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Beast")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Rocket")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Dunder")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Lacross")
	Our__Result = Add__Element__To__Set(Sample__Set__1,"Feast")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Dunder")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Lacross")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Feast")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Beast")
	Our__Result = Add__Element__To__Set(Sample__Set__2,"Rocket")
	print("Sample Set 1", Sample__Set__1)
	print("sample set 2", Sample__Set__2)
	Set_Intersection(Sample__Set__1, Sample__Set__2)
	print("\n")