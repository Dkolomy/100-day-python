
bidding_record = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bidding_record[name] = bid
  if input("Are there any other bidders? Type 'yes' or 'no'. ") == "no":
    bidding_finished = True

highest_bid = 0
for name in bidding_record:
  if bidding_record[name] > highest_bid:
    highest_bid = bidding_record[name]
    winner = name

print(f"The winner is {winner} with a bid of ${highest_bid}")
