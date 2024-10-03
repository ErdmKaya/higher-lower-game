# Simple Higher or Lower Game
import art
import random
from game_data import data

print(art.logo)
# comparison of 2 account - getting from game_data
def compare_followers():
    comparison1 = random.randint(0, len(data) - 1)
    comparison2 = random.randint(0, len(data) - 1)

    # prevents the two from being the same
    while comparison1 == comparison2:
        comparison2 = random.randint(0, len(data) - 1)

    print(f'Compare A: {data[comparison1]["name"]}, a {data[comparison1]["description"]}, from {data[comparison1]["country"]}')
    print(art.vs)
    print(f'Against B: {data[comparison2]["name"]}, a {data[comparison2]["description"]}, from {data[comparison2]["country"]}')

    return comparison1, comparison2

# game starting function
def play_game():
    score = 0
    is_game = True

    # getting input from user
    while is_game:
        comparison1, comparison2 = compare_followers()
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Comparison
        if guess == 'a':
            if data[comparison1]["follower_count"] > data[comparison2]["follower_count"]:
                score += 1
                print(art.logo)
                print(f"You're right! Current score = {score}")
            else:
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                is_game = False
        elif guess == 'b':
            if data[comparison2]["follower_count"] > data[comparison1]["follower_count"]:
                score += 1
                print(art.logo)
                print(f"You're right! Current score = {score}")
            else:
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                is_game = False

if __name__ == "__main__":
    play_game()