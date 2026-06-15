game_level = 3

# No Block Scope
if game_level < 5:
  new_enemy = "Easy"

print(new_enemy)

# def is_prime(num):
#   if type(num) != int or num <= 1:
#     return False

#   for i in range(2, num - 1):
#     if num % i == 0:
#       return False
#   return True

# for i in range(1, 10):
#   if is_prime(i):
#     print(i)

# --------------
enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")