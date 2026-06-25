# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [Name] placeholder with the actual name.
# Save the letters in the folder "Output/ReadyToSend".

with open("./Input/Names/invited_names.txt") as names_file:
  names = names_file.readlines()
  for name in names:
    with open("./Input/Letters/starting_letter.txt") as letter_file:
      letter = letter_file.read()
      letter = letter.replace("[name]", name.strip())
      with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.docx", mode="w") as output_file:
        output_file.write(letter)
