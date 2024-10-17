# Write a single line of Python Code that would satisfy this situation:
# You're ordering supplies from a store and you need to figure out what total price is.  
# The Supplies cost $10. You have a 30% Discount at this store, State tax is 5% and shipping will be 7.50

total = (10-(10*0.3)) + (*0.05) + 7.50

# a is cost
# b is discount
# c is state tax
# d is shipping
# t is total 
# x is subtotal

a = 10
b = 0.3
c = 0.05
d = 7.50
x = a - (a*b)

# This is the one line of equation to run for full total:

t = x + (x*c) + d

print t 
