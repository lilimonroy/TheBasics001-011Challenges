#----------* CHALLENGE 4 *----------
#Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].

num1 = int(input("Enter a integer number: ")) #We add "int" before "input", because it allows manipulete data as integers.
num2 = int(input("Enter a second integer number: "))
total = num1 + num2

print("The total is: ", total)