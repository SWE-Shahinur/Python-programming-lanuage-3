#element list a kotobar ase ta count kore
#counter ta import kore nite hoykl,ist,tuple,string rakha jay

from collections import Counter
s='shahinur'
print(Counter(s))
s1=({1,3,'g','j'})
print("set counter",Counter(s1))
num=[1,2,3,1,2]
print("list",Counter(num))



#OR
n=Counter((1,2,1))
print(n)
print(type(n))


print(issubclass(Counter,dict))

#aksathe akadik list/tupe/string pathate parbo na argument hisebe
'''aitae error dekhabe '''
'''c=Counter([1,2],[3,4])
print(c)'''



#counter updating

print("counter updating")
c=Counter()
print(c)
c.update('a')
print(c)
c.update('aab')
print(c)

#counter delet
print("counter delet")
c.subtract('a')
print(c)

#counter axcesssinh
print('counter axcessinh')
print(c['d'])
print(c['a'])
                                                                                                                                                                                                                                                                                                                                                                                