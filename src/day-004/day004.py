import random
import module004

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(module004.my_number)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# -----------------
fruits = ["Apple", "Banana", "Cherry"]
random_fruit = random.choice(fruits)
print(random_fruit)
print(fruits[-1])

print(fruits)
fruits.append("Orange")
print(fruits)

fruits.extend(["Pineapple", "Mango"])
print(fruits)