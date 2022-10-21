name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P2_Mediate"


# =======================================================================
# divisor_game(n, player1, player2)
#
# Mediates the divisor game starting with postive integer n
# between player1 and player2 (both are strings of their names).
#
# This function has no return value.
# =======================================================================
def make_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def eliminate(n, divisors):
    return [d for d in divisors if n % d != 0]


def get_int(prompt, divisor_list):
    failed = False
    while True:
        try:
            if failed:
                prompt = "Please enter a number in the list: "
            pick = int(input(prompt))
            if pick not in divisor_list:
                raise ValueError
            return pick

        except ValueError:
            failed = True


def divisor_game(n, player1, player2):
    turn_count = 0
    divisor_list = make_divisors(n)
    while len(divisor_list) > 0:
        print(f"Here are the remaining numbers: {divisor_list}")
        if turn_count % 2 == 0:
            pick = get_int(
                f"{player1}, pick a number from the list above: ", divisor_list
            )

        else:
            pick = get_int(
                f"{player2}, pick a number from the list above: ", divisor_list
            )
        divisor_list = eliminate(pick, divisor_list)

        turn_count += 1
    if turn_count % 2 == 0:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    print(f"{loser}, you lose! {winner}, you win!")


# =======================================================================
# Main program below (do not alter!)
# =======================================================================

print()
print(name)
print(header1)
print(header2)
print()

print("\nWelcome to the Divisor Game!")
player1 = input("\nPlayer 1, enter your name:  ")
player2 = input("Player 2, enter your name:  ")

n = int(input("Enter positive integer n:  "))

while n > 0:
    divisor_game(n, player1, player2)
    print("=========================================================")
    n = int(input("\n\nEnter positive integer n to play again (or 0 to quit):  "))

print("\nBye!")
