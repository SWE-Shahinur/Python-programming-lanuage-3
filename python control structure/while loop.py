#while loop a condition true hle exicute kori
a=10
while a>0:
    print('valu of a is',a)
    a=a-2
print('loop is complete')

#another example
n=153
total=0
while n>0:
    r=n%10
    total+=r
    n=n/10
print(total)