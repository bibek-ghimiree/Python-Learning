text = "Hello Python"

print(text[0])        # H
print(text[-1])       # n
print(text[0:5])      # Hello
print(len(text))
print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))


message = "  learn python  "

print(message.strip())
print(message.title())
print(message.capitalize())
print(message.startswith("  learn"))
print(message.count("n"))

words = "apple,banana,mango".split(",")
print(words)

joined = "-".join(words)
print(joined)


#f-string

name = "Ram"
age = 20

print(f"My name is {name} and I am {age} years old.")