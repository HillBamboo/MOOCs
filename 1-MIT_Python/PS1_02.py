s = raw_input()
cnt = 0 
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        cnt += 1
print 'Number of times bob occurs is: %d'%cnt
