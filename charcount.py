print('Welcome in char count program....')
s = input('Enter the string:')
n = len(s)
output = ''
count = 1
for i in range(n-1):
    if s[i]==s[i+1]:#if first word and previous word are same then increase count
        count+=1
    else:
        output =output+str(count)+s[i]# if previous and present word not same then count =1
        count =1
output = output+str(count)+s[n-1] # count last char
print(output)