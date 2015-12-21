#Test Case 1:
			#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
	      #balance = 4213
	      #annualInterestRate = 0.2
	      #monthlyPaymentRate = 0.04
	      
	      #Result Your Code Should Generate:
	      #-------------------
	      #Month: 1
	      #Minimum monthly payment: 168.52
	      #Remaining balance: 4111.89
	      #Month: 2
	      #Minimum monthly payment: 164.48
	      #Remaining balance: 4013.2
	      #Month: 3
	      #inimum monthly payment: 160.53
	      #Remaining balance: 3916.89



balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minMonthlyPayment = 0.0
unpaidBalance = balance
 
total = 0.0
for i in range(1, 13):
	print 'Month:', i
	minMonthlyPayment = monthlyPaymentRate * balance
	print 'Minimum monthly payment: %.2f' % minMonthlyPayment
	total += minMonthlyPayment
	balance -= minMonthlyPayment
	balance *= (1 + annualInterestRate / 12)
	print 'Remaining balance: %.2f' % balance
print 'Total paid: %.2f' % total
print 'Remaining balance: %.2f' % balance
