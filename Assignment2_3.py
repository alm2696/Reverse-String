input_string = input("Enter a string: ")

reversed_a = ""

for char in input_string:
    reversed_a = char + reversed_a

reversed_b = input_string[::-1]

print("Reversed string using a loop:", reversed_a)
print("Reversed string using slicing:", reversed_b)