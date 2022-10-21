import math  # use math.inf and -math.inf for infinity and negative infinity

name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P4_Minimax"


# =======================================================================
# COPY YOUR FUNCTION "divisor_game_agent(n, name, turnNum, agent)" here:
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
            pick, nodes_visited = agent(divisor_list)
            print(f"Agent picked {pick}")
            print(nodes_visited)

        divisor_list = eliminate(pick, divisor_list)

        turn_count += 1
        print()
    if (1 + turnNum + turn_count) % 2 == 0:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    print(f"{loser}, you lose! {winner}, you win!")


#


# =======================================================================
# DG_Max_Value:
# nn
# Input: divsors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the maximum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves maximum utility
#          numNodes = number of nodes examined (including the current node) to determine this


def DG_Max_Value(divisors):
    if len(divisors) == 0:
        return [1, -1, 1]
    max_u = -69_420
    total_nodes_visited = 1
    return_action = -1111111
    for action in divisors:
        utility, nah, nodes_visited = DG_Min_Value(eliminate(action, divisors))
        max_u = max(utility, max_u)
        if utility == max_u:
            return_action = action
        total_nodes_visited += nodes_visited
    return [max_u, return_action, total_nodes_visited]


# =======================================================================
# DG_Min_Value:
#
# Input: divsors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the minimum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves minimum utility
#          numNodes = number of nodes examined (including the current node) to determine this


def DG_Min_Value(divisors):
    min_u = 69_420
    if len(divisors) == 0:
        return [0, -1, 1]
    min_u = 69_420
    total_nodes_visited = 1
    return_action = -1111111
    for action in divisors:
        utility, nah, nodes_visited = DG_Max_Value(eliminate(action, divisors))
        min_u = min(utility, min_u)
        if utility == min_u:
            return_action = action
        total_nodes_visited += nodes_visited
    return [min_u, return_action, total_nodes_visited]


# =======================================================================
# Don't alter anything below here!
def DG_Agent(divisors):
    utility, action, numNodes = DG_Max_Value(divisors)
    return action, f"(Agent visited {numNodes} nodes to determine this.)"


print()
print(name)
print(header1)
print(header2)
print()

print("Welcome to the Divisor Game, version MINIMAX!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, DG_Agent)
