#----------* CHALLENGE 8 *----------
#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

bill = int(input("What's the total price of the bill?: "))
diners = int(input("How many diners there are?: "))

eachOne = bill // diners

print("Each person should pay:", eachOne)