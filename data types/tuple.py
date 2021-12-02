#tuple & list er modde basic parthokko hosse tuple priborton krajay na
#tuple () use hoy,
#tuple update
tup1=('a','b','c')
tup2=(1,2,3)
tuple=tup1+tup2
print(tuple)

#tuple lenth
print("tuple lenth:",len(tup1))

#tuple repitation
print("tuple repitation:",tup2*2)


#tuple max,min
print(tup2)
print("max:",max(tup2))
print('min:',min(tup2))

#membershi -element ei tuple er modde ase ki na
print("tuple membership:",5 in tup2)

#axcessing,indexing,slicing in tuple
print(tup2)
print("indexing:",tup2[1])
print("indexing:",tup2[-1])
print('slicing:',tup2[1:]) #1 theke start then baki sob gula
print("slicing:",tup2[:2]) #0 theke start then 2 index porjonto
print("slicing:",tup2[1:3]) # 1 theke start then 3 index porjonto
#tuple delet korle purota delet hye jay
del(tup1)
