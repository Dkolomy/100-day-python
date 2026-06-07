hello = "Hello World"
print(hello[0])
print(hello[1])
print(hello[-1])

print(123_456_789)

print(type(123_456_789))
print(type(hello))
print(type(123_456_789.01))
print(type(True))

# print("Length is " + str(len(input("What is your name?"))))

print(type(123 + 456)) # <class 'int'>
print(type(7 - 3)) # <class 'int'>
print(type(7 - 3.2)) # <class 'float'>
print(type(3 * 2)) # <class 'int'>
print(type(6 / 3)) # <class 'float'>
print(type(6 // 3)) # <class 'int'>

bmi = 80 / 1.75 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")