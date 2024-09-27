
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)