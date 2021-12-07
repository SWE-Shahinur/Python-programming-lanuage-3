#ojana sokhkk argumenter jonno er jonno variable lenth argument use kra hoy

def greet(*names):
    '''this '*' convert the argument into variable lenth argument'''
    for i in names:
        print('hello',i)
print(greet('shahinur','sharmin','ameerah','ahmed'))

