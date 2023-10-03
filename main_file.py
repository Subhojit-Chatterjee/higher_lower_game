import random
from art import logo, vs
from game_data import data


"""The following function returns the data of a random account"""


def get_account_data():
    return random.choice(data)


"""The following function checks wether the user's guess is correct or not and returns 'True' for correct guess
 and 'False' for incorrect guess """


def check_answer(follower_1, follower_2, guess):
    if follower_1 > follower_2:
        correct_answer = 'a'
        return guess == correct_answer
    else:
        correct_answer = 'b'
        return guess == correct_answer


"""The following function provides a formatted version of the data extracted from the account to be printed on
 the console"""


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} a {description} from {country}"


def higher_lower_game():
    score = 0
    game_should_continue = True
    account_a = get_account_data()
    account_b = get_account_data()
    while game_should_continue:
        account_a = account_b
        account_b = get_account_data()

        while account_a == account_b:
            account_b = get_account_data()

        clear()
        print(logo)
        print("\n\nWelcome to the Higher Lower Game\n\n")
        print("A. " + format_data(account_a) + vs + "\nB. " + format_data(account_b))
        user_guess = input("\nWho has more followers? Type 'A' or 'B' : ").lower()

        follower_a = account_a["follower_count"]
        follower_b = account_b["follower_count"]

        if check_answer(follower_a, follower_b, user_guess):
            score = score + 1
            print(f"\nRight answer! Your score is {score}")
            game_should_continue = True
        else:
            print(f"\nWrong answer! You lose... Your final score is {score}")
            game_should_continue = False


higher_lower_game()
