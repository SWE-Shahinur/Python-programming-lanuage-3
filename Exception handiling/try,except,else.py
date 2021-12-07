my_list=[1,3,4,5,6]
try:
    print(my_list[4])
except IndexError:
    print("index valu exceeded")
else:
    print("executed sucseddfully")
finally:
    print('whatever happend i will be executed')