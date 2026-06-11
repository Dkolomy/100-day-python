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
      new_letter = alphabet[new_position]
      encrypted_text += new_letter

  print(f"Here is encoded result: {encrypted_text}")

def decrypt(text, shift):
  decrypted_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position - shift
      new_letter = alphabet[new_position]
      decrypted_text += new_letter

  print(f"Here is decoded result: {decrypted_text}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("Invalid direction")