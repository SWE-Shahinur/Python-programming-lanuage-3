#list a diffrent type deta rakha jay,[] diye likha hoy
#list connecting
listA=['a','b','c','d']
listB=[1,2,3]
print("conenting:", listA+listB)

#slicing -akadik sublist creat kra jay
list=[1,5,4,7,8,9]
print("slicing:", listA[1:])
print(list[:3])
print("slicing: ",list[1:4]) # 1 theke then koto ta rakhbe


#list updating but deta ta replace kore
print(list)
list[2]=10
print("list updating:" , list)

#APPENDING list a 1ti kore deta input korte pari
l=[1,2,3,4,5,5]
l.append(6)
print("apending:",l)

#delet/remove 1ti kore deta remove kora jay
l.remove(4)
print("remove 4: ",l)
l.remove(5)
print("only 1 5 remove:",l)


#list lenth  use lem()
print(l)
print("list lenth",len(l))

#repitation -akadikbar output chaile normalgun kredilei hoy
print("repitation:",l*2)

#list er max & min ber korte chaile
print("list max:",max(l))
print("list min:",min(l))


#membership 1ti element lister member kina ta check kra hoy row keyword dara
lists=[2,3,4,5]
print("membership:",1 in lists)ty
