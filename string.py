str="DevOps"
print(str)
print("Spliting Words")
text = "apple-banana-orange-grape"  
print(text)
fruits = text.split('-', maxsplit=2)  
print(fruits) 
print("String Formating")
name = "Alice"  
age = 30  
greeting = f"Hello, my name is {name} and I'm {age} years old."  
print(greeting)
print("Eliminating Unnecessary Characters in String")  
text = "!!!Hello, World!!!"  
print(text)
clean_text = text.strip("!")  
print(clean_text)  
print("Concatenate Strings")
string1 = "Development"  
string2 = "Operation"
print(string1)
print(string2)  
result = string1 + " " + string2  
print(result)  
print("Delimeter")
delimiter = " "  
my_list = ["apple", "banana", "cherry"]  
print(my_list)
result = delimiter.join(my_list)  
print(result)  
