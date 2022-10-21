name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P3_SimpleAgent"


# =======================================================================
# divisor_game_agent(n, name, turnNum, agent)
#
# Mediates the divisor game starting with postive integer n
# between a human named "name" and agent "agent", which is a function that takes a list
# of the remaining divisors and returns one of them.
#
# turnNum = 1 if the human wants to go first, 2 if the human wants to go second.
#


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


def divisor_game_agent(n, name, turnNum, agent):
    turn_count = 0
    divisor_list = make_divisors(n)
    player1 = name
    player2 = "Agent"
    while len(divisor_list) > 0:
        print(f"Here are the remaining numbers: {divisor_list}")
        if (1 + turnNum + turn_count) % 2 == 0:
            pick = get_int(
                f"{player1}, pick a number from the list above: ", divisor_list
            )

        else:
            pick = agent(divisor_list)
            print(f"Agent picked {pick}")

        divisor_list = eliminate(pick, divisor_list)

        turn_count += 1
    if (1 + turnNum + turn_count) % 2 == 0:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    print(f"{loser}, you lose! {winner}, you win!")


# =======================================================================
# Don't alter anything below here!

# =======================================================================
# Simple agent always picks first number in list


def simple_agent(divisors):
    return divisors[0]


# =======================================================================
# Main program:

print()
print(name)
print(header1)
print(header2)
print()

print("Welcome to the Divisor Game!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, simple_agent)
