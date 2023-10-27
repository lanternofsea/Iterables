# Task 1 
# Join the strings in the list below using the "*" character 
# Use <str>.join() on line 6, so that the resulting string is stored in the variable result1
# Expected Output: Today*is*a*Sunday 
a_list = ["Today", "is", "a", "Sunday"]

result1 = "*".join(a_list)
print(result1)

# Task 2
# Convert the string below to Title Case using <str>.title() on line 18
# Split the string at the "space" character using <str>.split() on line 21
# Expected Output 1: "I Love Green Day"
# Expected Output 2: ["I", "Love", "Green", "Day"] 

a_string = "i love green day"

title_string = a_string.title()
print(title_string)

string_list = title_string.split(" ")
print(string_list)

# Task 3
# populate the variable a_tuple below with a tuple of 3 numbers on line number 28
# Expected Example Output 1: (1, 2, 1000)

a_tuple = (1, 2, 1000)
print(a_tuple)

a, b, c = a_tuple
print(a)
print(b)
print(c)