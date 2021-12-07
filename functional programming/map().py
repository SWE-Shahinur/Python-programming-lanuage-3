def celcious_to_fahrenheit(tem_in_celcious):
    temp=(tem_in_celcious*1.8)+32
    return temp
list_of_temp=[20,2,24,32,35,28,30]
for i in list_of_temp:
    print(celcious_to_fahrenheit(i))
print(list(map(celcious_to_fahrenheit,list_of_temp)))


#using map,akadik itarable obj jonno map()
a=(3,4,5,6)
b=(4,5,6,7,8)
print(list(map(lambda x,y:x+y,a,b)))