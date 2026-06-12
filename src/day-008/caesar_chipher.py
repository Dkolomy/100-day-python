alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      new_letter = alphabet[new_position % len(alphabet)]
      encrypted_text += new_letter

  print(f"Here is encoded result: {encrypted_text}")

def decrypt(text, shift):
  decrypted_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position - shift
      if new_position < 0:
        new_position = len(alphabet) + new_position
      else:
        new_position = new_position % len(alphabet)
      new_letter = alphabet[new_position]
      decrypted_text += new_letter

  print(f"Here is decoded result: {decrypted_text}")

def caesar(text, shift, direction):
  new_text = ""
  if direction == "decode":
    shift *= -1

  for letter in text:

    if letter not in alphabet:
      new_text += letter
    else:     
      position = alphabet.index(letter)
      position = alphabet.index(letter) + shift
      position %= len(alphabet)
      new_text += alphabet[position]

  print(f"Here is the {direction}d result: {new_text}")

# if direction == "encode":
#   encrypt(text, shift)
# elif direction == "decode":
#   decrypt(text, shift)
# else:
#   print("Invalid direction")

caesar(text, shift, direction)