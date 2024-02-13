import random

from replit import clear
from art import logo, vs
from game_data import data


def choose_data(data_bank):
    """gets a random data from game_data """
    chosen_data = random.choice(data_bank)
    return chosen_data


def get_b_bucket(bucket_a, data_bank):
    """gets data specifically for b_bucket and making sure it doesn't match bucket_a data"""
    bucket_b = choose_data(data_bank)
    while bucket_b == bucket_a:
        bucket_b = choose_data(data_bank)
    return bucket_b


def compare(bucket_a, bucket_b):
    """compare and returns which bucket has more followers"""
    if bucket_a["follower_count"] > bucket_b["follower_count"]:
        return bucket_a
    else:
        return bucket_b


def display_choices(bucket_a, bucket_b):
    """Displays Bucket A and Bucket B for user to choose/guess. """
    print(f"Compare A: {bucket_a["name"]}, {bucket_a["description"]}, from {bucket_a["country"]}")
    print(vs)
    print(f"Against B: {bucket_b["name"]}, {bucket_b["description"]}, from {bucket_b["country"]}")


def user_guess_check(user_choice, winner_bucket, current_score):
    """Checks if user guess right or wrong. Returns a boolean for game_over loop, and the current score"""
    if user_choice == winner_bucket:
        clear()
        current_score += 1
        print(logo)
        print(f"You're right! Current score: {current_score}")
        return False, current_score
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        return True, current_score


play_again = True

while play_again:

    score = 0
    a_bucket = choose_data(data)
    b_bucket = get_b_bucket(a_bucket, data)
    game_over = False

    print(logo)

    while not game_over:

        display_choices(a_bucket, b_bucket)

        # Assigns a bucket data to user_guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_guess == "A":
            user_guess = a_bucket
        elif user_guess == "B":
            user_guess = b_bucket

        current_bucket_winner = compare(a_bucket, b_bucket)

        game_over, score = user_guess_check(user_guess, current_bucket_winner, score)

        if not game_over:
            # a_bucket will receive b_bucket's data while b_bucket will have a new data
            a_bucket = b_bucket
            b_bucket = get_b_bucket(a_bucket, data)

    if input("Do you want to play again? Type 'y' for Yes and 'n' for No: ").lower() == "n":
        play_again = False
