my_list=[1,2,3,4,5,6]
try:
    print(my_list[4])
except IndexError:
    print('index valu exceeded')
finally:
    print(' whatever happend i will be executed')