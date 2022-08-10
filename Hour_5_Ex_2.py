first_name = ""
last_name = ""
widget_name = ""
widget_count = ""
price = ""
subtotal = ""
total = ""
printout1 = "Thank you for your purchase {} {}"
printout2 = "What kind of Widget are you buying? {}"
printout3 = "How many widgets are you buying? {}"
printout4 = "How much do they cost, per item? {}"
printout5 = "Your total is ${}"
printout6 = "Thank you for shopping with us {} {}"

first_name = raw_input('Give me your first name, please: ')
first_name = first_name.strip()
first_name = first_name.title()

last_name = raw_input('Give me your last name, please: ')
last_name = last_name.strip()
last_name = last_name.title()

widget_name = raw_input('Please let us know what widget are you buying: ')
widget_name = widget_name.strip()
widget_name = widget_name.title()

widget_count = raw_input('Please let us know how many widgets are you buying: ')
widget_count = widget_count.strip()
widget_count = float(widget_count)

price = raw_input('What is the price per widget: ')
price = price.strip()
price = float(price)

subtotal = (widget_count * price)
total = round(subtotal,2)


print printout1.format(first_name, last_name)
print printout2.format(widget_name)
print printout3.format(int(widget_count))
print printout4.format(price)
print printout5.format('{:.2f}'.format(total))
print printout6.format(first_name, last_name)

