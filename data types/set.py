#deta akadikbar rakhte chaileo python akbar krei rakhbe
set={'a','b','c','a'}
print(set)
print(type(set))

#update a akadik elemet addkra jay
print('set udpate')
set.add('e') #add a jut 1 element
print(set)

set.update('e','f','g')
print(set)

#deleting a discard,remove,pop-last element use hoy
print("set deleting")
a={'a','b','c','d'}
a.pop()
print(a)
a.remove('b')
print(a)
a.discard('d')
print(a)


#set union-2 ba totodik aksathe jug krar jonno
print('set union')
m={1,2,3,2,9}
n={4,5,6,3,2}
print(m|n)
print('inersection',m&n)
print('set deferance:',m-n)#set theke bad deoa

p={'a','k','d'}
l={'w','s'}
print('a' in p)
print(p<l)

#frozenset-jomatoddo ja priborton korte dey na
p=frozenset()
#akhn r add kra jabe na add korle error dekhabe
'''p.add(3)
print(p)'''

