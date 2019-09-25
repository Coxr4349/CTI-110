# This is a meal tip, tax, and price calculator
# 091619
# CTI-110 P2HW1 - Meal Tip Calculator
# Ryan Cox

# get variable inputs
mealPrice = float(input('Enter meal price: '))
tipPercent = float(input('Enter the % tip as a decimal value: '))
taxRate = float(input('Enter tax rate as a decimal value: '))

# run calculations
mealTip = (mealPrice * tipPercent)
mealTax = (mealPrice * taxRate)
totalPrice = mealPrice + mealTax + mealTip

# Display results accordingly
print('Tip amount = $', format(mealTip, ',.2f'))
print('Tax amount = $', format(mealTax, ',.2f'))
print('Total meal price is $', format(totalPrice, ',.2f'))


# input the meal Price
# input the tip Percent as decimal
# input the tax Rate as decimal
# calculate meal tip as meal price times tip percent
# claculate meal tax as meal price times tax rate
# calculate total Price as meal price plus meal tip plus meal tax
# display the calculated tip
# display the calculated tax
# display the total meal price

