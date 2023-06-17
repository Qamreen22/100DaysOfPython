from replit import clear
import art.py
#HINT: You can call clear() to clear the output in the console.
print(art.logoAuc)
print("Welcome to the secret auction!")
dictionary = {} 
is_next = 'yes'
while(is_next == 'yes'):
    name = input("What is your name?: ")
    bid = int(input("How much would you like to bid?: $"))
    dictionary[name]=bid;
    is_next = input("Are there any other bidders? Type 'yes' or 'no': ")
    clear()

max_bid = 0
for name in dictionary:
    if dictionary[name] > max_bid:
        max_bid = dictionary[name]
        max_bidder = name

print(f"The winner is {max_bidder} with a bid of ${max_bid}")
        
    