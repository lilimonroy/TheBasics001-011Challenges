#----------* CHALLENGE 11 *----------
#Task the user to enter a number over 100 and then enter a number under
#10 and tell them how many times the smaller number goes into the larger
#number in a user-friendly format.

#firstNumber = int(input("Enter a number over 100: "))
#secondNumber = int(input("Enter a second number under 10: "))

#howMany =firstNumber//secondNumber

#print("The fisrt number \"",firstNumber,"\", fits",howMany,"times the second number \"",secondNumber,"\"." )

larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger//smaller
print(smaller,"goes into",larger,answer,"times")