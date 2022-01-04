#----------* CHALLENGE 6 *----------
#Ask how many slices of pizza the user started with and ask how many slices they have eaten. 
# Work out how many slices they have left and display the answer in a user-friendly format.

slicesBeforeEaten = int(input("Enter how many slices has the pizza: "))
slicesTheyEaten = int(input("Enter how any slices have you eaten: "))

slicesAfterEaten = slicesBeforeEaten - slicesTheyEaten

print("Now we just have ",slicesAfterEaten," slices of pizza.")
