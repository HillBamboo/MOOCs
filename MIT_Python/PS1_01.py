s = raw_input()
cnt = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt +=1
print 'Number of vowels: %d'%cnt
