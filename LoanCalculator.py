#get the total monew owed from the customer 
moneyOwed = float(input('Enter the total amount of load you have taken '))
#get the anual rate of intrest 
intrest = float(input('Enter the annual rate of intrest'))
#get the monthly payment done by the customer 
monthlyPyment= float(input('Enter the amount you will be paying every month'))
#get the no of months to calculat the loan amount
months = int(input('Enter the no of month  '))

#divide intrest by 100 to get the percentage , than by 12 to get monthly intrest 

rate = intrest/100/12


for i in range(months):
    interestPayed = moneyOwed * rate
    moneyOwed = moneyOwed+interestPayed

    moneyOwed =moneyOwed - monthlyPyment

print('Money I owe still  ',moneyOwed)

