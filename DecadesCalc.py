yourAge = int(input('What is you age \n'))
calcDecade = yourAge // 10
CalcYear = (yourAge % 10 )
result = "Your age in decades is " + str(calcDecade) + " and " + str(CalcYear) + " years" 
print(result)