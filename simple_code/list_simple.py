sales_w1= [7,3,42,19,15,35,9]
sales_w2= [12,4,26,10,7,28,]
sales_w2.append(10)
print(sales_w1)
print(sales_w2)
sales_w1.extend(sales_w2)
sales=sales_w1.copy()
print(sales)
print(sum(sales))
print(max(sales))
print(min(sales))
a=1.5
bd= a * max(sales)
wd= a * min(sales)
print(bd)
print(wd)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
#sales = sales_w1 + sales_w2
sales.sort()
#worst_day_prof = sales[0] * 1.5
#best_day_prof = sales[-1] * 1.5
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')