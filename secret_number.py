secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int (input("Guess the number: "))

while number != secret_number:
    print ("Ha ha! You're stuck in my loop!")
    number = int (input("Guess number again: "))

print ("Well done, muggle! You are free now. End of game")
print("You won!")