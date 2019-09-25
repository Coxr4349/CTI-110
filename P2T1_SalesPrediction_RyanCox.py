# This is a profit prediction calculator
# 091119
# CTI-110 P2T2 - Sales Prediction
# Ryan Cox

#get value of projected sales
totalSales = float(input('Enter projected sales:'))

#calculate profit
profit = totalSales * 0.23

#display projected profit
print('The profit is $', format(profit, ',.2f'))
