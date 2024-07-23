import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
game_on = input("Want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while game_on == "y":
    user_card_1 = random.randint(0, 12)
    user_card_2 = random.randint(0, 12)
    user_cards = [user_card_1, user_card_2]
    user_score = sum(user_cards)
    computer_card_1 = random.randint(0, 12)
    computer_card_2 = random.randint(0, 12)
    computer_cards = [computer_card_1, computer_card_2]
    computer_score = sum(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_card_1}")

    while user_score < 21:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == "y":
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)
            if user_score > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_score = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        elif draw_card == "n":
            break
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win.")
    elif user_score == computer_score:
        print("It's a draw.")
    elif user_score == 21:
        print("You win with a Blackjack.")
    elif computer_score == 21:
        print("Computer wins with a Blackjack.")
    elif user_score > computer_score:
        print("You win.")
    else:
        print("You lose.")
    game_on = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    if game_on == "y":
        os.system('clear')
        print(art.logo)
print("Goodbye!")