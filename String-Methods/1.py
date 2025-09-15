text = "   welcome to PYTHON programming 101!   "
print('[' + text.strip() + ']')
print()

print('[' + text.capitalize() + ']')
print()

print('[' + text.upper() + ']')
print()

print('[' + text.lower() + ']')
print()

print('[' + text.title() + ']')
print()

print('[' + text.swapcase() + ']')
print()

print('[' + text.center(50, '-') + ']')
print()

print(text.count("o"))
print()

print('[' + text.replace("PYTHON", "Java") + ']')
print()

print(text.split())
print()
print()
print()
print()

# __________________________________________________________________________________________

print(text.startswith("welcome"))
print()

print(text.endswith("101!   "))
print()

print(text.isalnum())
print()

print(text.isalpha())
print()

print(text.islower())
print()

print(text.isupper())
print()

print(text.isspace())
print()
print()
print()
print()

# __________________________________________________________________________________________

print("cat" == "cat")
print()

print("cat" != "cat")
print()

print("cat" < "caterpillar")
print()

print("dog" > "Dog")
print()

print("10" == 10)
print()

print("10" != 10)
print()
print()
print()
print()

# __________________________________________________________________________________________

words = ("dog", "cat", "zebra", "ant")
print(words)
new_words = sorted(words)
print(new_words)

list = ["dog", "cat", "zebra", "ant"]
list.sort()
print(list)
print()
print()
print()
print()

# __________________________________________________________________________________________

num = 100
num_ = str(num)
print(type(num_))

num1 = "200"
num1_ = int(num1)
print(type(num1_))

num2 = "300.5"
num2_ = float(num2)
print(type(num2_))

int("hello")