name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P3_SimpleAgent"


#=======================================================================
# divisor_game_agent(n, name, turnNum, agent)
#
# Mediates the divisor game starting with postive integer n 
# between a human named "name" and agent "agent", which is a function that takes a list
# of the remaining divisors and returns one of them.
#                                                           
# turnNum = 1 if the human wants to go first, 2 if the human wants to go second.
#

def divisor_game_agent(n, name, turnNum, agent):





#=======================================================================
# Don't alter anything below here!

#=======================================================================
# Simple agent always picks first number in list

def simple_agent(divisors):
   return divisors[0]
#=======================================================================
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
   



