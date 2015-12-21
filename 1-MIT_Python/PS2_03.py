'''Monthly interest rate = (Annual interest rate) / 12.0
   Monthly payment lower bound = Balance / 12
   Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0'''
def myTest(balance, annualInterestRate):
	"""
	Input: balance and annualInterestRate
	Output:Return Lowest Payment 
	Example:
		>>> myTest(320000, 0.2)
		Lowest Payment: 29157.09
		>>> myTest(999999, 0.18)
		Lowest Payment: 90325.03
	"""
	monthlyInterestRate = annualInterestRate / 12.0
	lo = balance / 12
	hi = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
	bTmp = balance
	while True:
		balance = bTmp
		minMonthlyPayment = (lo + hi) / 2
		for i in range(12):
			balance -= minMonthlyPayment
			balance *= (1 + monthlyInterestRate)
		if abs(balance) <= .06: break
		elif balance > 0: lo = minMonthlyPayment
		else: hi = minMonthlyPayment
	print "Lowest Payment: %.2f" % minMonthlyPayment
