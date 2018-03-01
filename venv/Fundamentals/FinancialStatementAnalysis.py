

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


#---- Profit -------- revenue - expenses----

profit = list([])

for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
profit

print(profit)


#----- tax ------ profit X 30% ------

tax = [round(i * 0.3, 2) for i in profit]
print(tax)

#---- profit after tax ------

profit_after_tax = list([])
for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])
print(profit_after_tax)

#------Profit  Margin after Tax -----

profit_margin = list([])
for i in range(0, len(profit)):
    profit_margin.append(round((profit_after_tax[i]/revenue[i]) *100,2 ))
print(profit_margin)


#----- Profit after tax mean -------

mean_profit_after_tax = sum(profit_after_tax) / len(profit_after_tax)
print(mean_profit_after_tax)


#------ Good month and bad months ------

good_months = list([])
bad_months = list([])
for i in range(0,len(profit)):
    if (profit_after_tax[i] > mean_profit_after_tax):
        good_months.append(True)
        bad_months.append(False)
    else:
        good_months.append(False)
        bad_months.append(True)


print(good_months)
print(bad_months)

#----- Best month ---------

best_month = list([])
worst_month = list([])
for i in range(0, len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
print(best_month)
print(worst_month)











