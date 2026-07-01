# FileNotFoundError
# try:
#   file = open("a_file.txt")
# except FileNotFoundError:
#   file = open("a_file.txt", "w")
#   file.write("Something")
# else:
#   file.read()
# finally:
#   file.close()

# KeyError

# try:
#   dictionary = {"key": "value"}
#   value = dictionary["non_existent_key"]
# except KeyError as error_message:
#   print(f"That key does not exist. {error_message}")
# else:
#   print("That key does not exist.")
# finally:
#   file.close()

# IndexError

# try:
#   fruit_list = ["Apple", "Banana", "Cherry"]
#   fruit = fruit_list[3]
# except IndexError as error_message:
#   print(f"That index does not exist. {error_message}")


