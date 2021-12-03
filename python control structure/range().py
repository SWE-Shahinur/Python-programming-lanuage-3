#range function start,end,increment-proti dape kot kore briddi pabe
print(range(5))
a=range(5)
print(type(range(5)))

for i in range(5): #akhane by default start value:0 and end value 1 dorece
    print(i)


#with start ,end
print("start,end,increment")
for i in range(1,10,2):
    print(i)

#range er maddome list create kra jay
number=list(range(10)) #range mulot akti object return kore
print(number)