# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# balance = 3329
# annualInterestRate = 0.2
# low = balance

# minMonthlyPayment = 10
#for i in range(12):
def myTest(balance, annualInterestRate):
	'''
	x: balance
	y: annualInterestRate
	Return Lowest Payment 
	'''
	bTmp = balance
	minMonthlyPayment = 0
	while True:
		balance = bTmp
		minMonthlyPayment += 10
		for i in range(1, 13):
			balance -= minMonthlyPayment
			balance *= (1 + annualInterestRate / 12)
		if balance <= 0: break
	print 'minMonthlyPayment: %.2f' % minMonthlyPayment
	print 'Remaining balance: %.2f' % balance




		
