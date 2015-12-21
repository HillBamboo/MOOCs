'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
# STEP1. lo = hi = 0
# STEP2. hi++ until that is going to be lower, recording the length
# STEP3. lo = hi + 1, repeating STEP1 until hi >= array.length
#Sorting!!!

def LSS(s):
	# max_len = 0
	# LI = 0
	# RI = 1
	# cnt = 0
	# lo, hi = 0, 0
	# while lo < len(s) - 1:
	# 	while hi < len(s) - 1:
	# 		if s[hi] > s[hi + 1]:
	# 			if hi - lo + 1 > max_len:
	# 				cnt += 1
	# 				print "cnt = ", cnt					
	# 				LI = lo
	# 				print "LI: ", LI
	# 				RI = hi + 1
	# 				print "RI: ", RI
	# 				max_len = RI - LI
	# 				print "max_len: ", max_len
	# 			else:
	# 				lo = hi + 1 
	# 				break
	# 		else:
	# 			continue
	# 		hi += 1
	# return s[LI:RI]
	# ansOfLB, ansOfRB, lo, hi, max_len = 0, 0, 0, 1, 0
	# while hi != len(s) - 1:
	# 	for hi in range(lo, len(s)):
	# 		if s[hi - 1] > s[hi]:
	# 			if hi - lo + 1 > max_len:
	# 				max_len = hi - lo + 1
	# 				ansOfRB, ansOfLB = hi, lo
	# 			else: break
	# 	lo = hi
	# return s[ansOfLB:ansOfRB]
	# ans = [0, 0]
	# max_len, lo = 0, 0
	# for hi in range(len(s) - 1):
	# 	if s[hi] > s[hi + 1]:
	# 		if hi - lo + 1 > max_len:
	# 			max_len = hi - lo + 1
	# 			lo = hi + 1
	# 			ans[0], ans[1] = lo, hi
	# 		else: lo = hi + 1
	# print ans
	# print lo, hi
	# return s[lo:hi]
	max_len, lo, LB, flag = 0, 0, 0, 0
	for hi in range(len(s) - 1):
		if s[hi] > s[hi + 1]:
			if hi - lo + 1> max_len:
				max_len = hi - lo + 1
				LB = lo
				flag = 1
			lo = hi + 1
	if flag == 0: return s[:]
	return s[LB:max_len + LB]
	
print LSS('azcbobobegghakl')             #Corrct!
print LSS('abcbcd')                      #Corrct!
print LSS('abcdefghijklmnopqrstuvwxyz')	 #Corrct!
print LSS('zyxwvutsrqponmlkjihgfedcba')  #Corrct!