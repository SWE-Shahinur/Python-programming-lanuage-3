#genarate function value creat kore,range() hlo genarate function
a=range(3)
print(a)
for i in a:
    print(i)

print('genarator')
def gen(end):
    for i in range(0,end+1,2):
        print(i)
data=gen(5)
print(data)
