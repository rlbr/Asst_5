name = "LASTNAME_FIRSTNAME"
header1 = "CS-355, Fall 2022"
header2 = "A5_P2_Mediate"


#=======================================================================
# divisor_game(n, player1, player2)
#
# Mediates the divisor game starting with postive integer n 
# between player1 and player2 (both are strings of their names).
#                                                           
# This function has no return value.
#=======================================================================

def divisor_game(n, player1, player2):





#=======================================================================
# Main program below (do not alter!)
#=======================================================================

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
   



