#Dictionaries - a dictionary is an unordered set of key-value pairs
dict1 = {} #creating an empty dictionary
 
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
 
dict1["IOS"] #returns "12.4"; extracting a value for a specified key
 
dict1["IOS"] = "12.3" #modifies an existing key-value pair
 
dict1["RAM"] = "128" #adds a new key-value pair to the dictionary
 
del dict1["Ports"] #deleting a key-value pair from the dictionary
 
len(dict1) #returns the number of key-value pairs in the dictionary
 
"IOS" in dict1 #verifies if "IOS" is a key in the dictionary
 
"IOS2" not in dict1 #verifies if "IOS2" is not a key in the dictionary
 
#Dictionaries - methods
dict1.keys() #returns a list having the keys in the dictionary as elements
 
dict1.values() #returns a list having the values in the dictionary as elements
 
dict1.items() #returns a list of tuples, each tuple containing the key and value of each dictionary pair
 
#Conversions between data types
str() #converting to a string
int() #converting to an integer
float() #converting to a float
list() #converting to a list
tuple() #converting to a tuple
set() #converting to a set
bin() #converting to a binary representation
hex() #converting to a hexadecimal representation
int(variable, 2) #converting from binary back to decimal
