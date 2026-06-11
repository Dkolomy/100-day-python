TRUE = "true"
LOVE = "love"

def calculate_love_score(name1, name2):
  both_names = name1.lower() + name2.lower()
  true_score = 0
  love_score = 0
  
  for letter in both_names:
    if letter in TRUE:
      true_score += 1
    if letter in LOVE:
      love_score += 1
  
  # print(f"{true_score * 10 + love_score}")
  return true_score * 10 + love_score

print(calculate_love_score("Angela Yu", "Jack Bauer"))
print(calculate_love_score("Kanye West", "Kim Kardashian"))
