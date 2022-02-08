import itertools

ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
ranks = [str(rank) for rank in ranks]

# for rank in ranks:
#    rank = str(rank)
print(ranks)

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

# for rank in ranks:
# for suit in suits:
#     print(rank,suit)

deck = [card for card in itertools.product(ranks, suits)]

print(deck)

for (index, card) in enumerate(deck):
    print(1 + index, card)

Cards_in_hand = 4
hands = [hand for hand in itertools.combinations(deck, Cards_in_hand)]

print(len(hands))
deck_num = len(deck)

print(f"There is {deck_num} cards in the deck")
print(f"The number of {Cards_in_hand} card hands that can be made with 52 cards is {len(hands)}")

"The formula for combinations with deck_num = dn and Cards_in_Hand = Cih, = (((dn-(CIH-1))*(dn-(CIH-2))*(dn-("
"CIH-3))....*(dn-(0))*(1/CIH!) "

