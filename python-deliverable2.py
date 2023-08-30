print("Welcome to the GC Fruit Market!")

name = input("What is your name?")
subtotal = 0

welcome_text = (f"Welcome," +name +"! Which Fruit would you like to buy?")

wants_another = "y"
apple_count = 0
grape_count = 0
orange_count = 0

while wants_another == "y":
  print(welcome_text)
  thislist = ["1. Apple", "2. Grape", "3. Orange"]
  for x in thislist:
      print(x)
  fruit_number = input(">")
  if fruit_number == "1":
        print("You bought 1 apple at $2")
        apple_count += 1
        subtotal = subtotal + 2
  if fruit_number == "2":
        print("You bought 1 grape at $1")
        grape_count += 1
        subtotal = subtotal + 1
  if fruit_number == "3":
        print("You bought 1 orange at $3")
        orange_count += 1
        subtotal = subtotal + 3
  wants_another = input("Would you like another piece of fruit?")

print(f"Order for {name}")
print(f"{apple_count} apple(s) at $2 a piece")
print(f"{grape_count} apple(s) at $1 a piece")
print(f"{orange_count} apple(s) at $3 a piece")

print(f"Subtotal: ${subtotal}")

tax = 5 / 100 * subtotal
print(f"5% tax: {tax}")

total = subtotal + tax
print(f"Subtotal: {total}")
