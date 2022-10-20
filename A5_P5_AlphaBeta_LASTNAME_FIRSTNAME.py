import math  # use math.inf and -math.inf for infinity and negative infinity

name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P5_AlphaBeta"


#=======================================================================
# COPY YOUR FUNCTION "divisor_game_agent(n, name, turnNum, agent)" here:
#

def divisor_game_agent(n, name, turnNum, agent):






#=======================================================================
# DG_Max_Value:  IMPLEMENTS ALPHA BETA PRUNING
#
# Input:   divsors = list of the remaining divisors
#          alpha   = a lower bound on the minimax value of the node
#          beta    = an upper bound on the minimax value of the node
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the maximum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves maximum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Max_Value(divisors, alpha, beta):
   

   



#=======================================================================
# DG_Min_Value:  IMPLEMENTS ALPHA BETA PRUNING
#
# Input:   divsors = list of the remaining divisors
#          alpha   = a lower bound on the minimax value of the node
#          beta    = an upper bound on the minimax value of the node
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the minimum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves minimum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Min_Value(divisors, alpha, beta):






#=======================================================================
# Don't alter anything below here!

print()
print(name)
print(header1)
print(header2)
print()

print("Welcome to the Divisor Game, version ALPHA-BETA!")

name = input("\nEnter your name:  ")
n = int(input("Enter positive integer n:  "))
turnNum = int(input("Enter 1 if you want to go first, 2 for second:  "))

divisor_game_agent(n, name, turnNum, DG_Max_Value)
   



