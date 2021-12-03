#enumerate hosse built in function,2 peramiter*iterable-num,str,list,tuple,start valu)
items=['apple','orange','mango']
enu_item=enumerate(items)
print(type(enu_item))
print(enu_item)

print('convert to list item')
print(list(enu_item))

#start paramiter
enu_item=enumerate(items,10)
print(list(enu_item))

#use a for loop over a collction
months=['jan','feb','march']
for i  in enumerate(months):
    print(i)
