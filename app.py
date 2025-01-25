# sum of all the elements in the list
l=[]
l=(input('Enter Values').split(' '))
a=[]
for i in l:
    a.append(int(i))
sum=0
for i in a:
    sum+=i
print(sum)