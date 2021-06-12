expenses= []
# can also use sum(expenses) to get the total
noOfExpenses = int(input('Enter the number of expenses '))

for x in range(noOfExpenses): 
    expenses.append(float(input('Enter the expenses ')))

total = sum(expenses)

print("Your Expenses",total,sep=' ')


