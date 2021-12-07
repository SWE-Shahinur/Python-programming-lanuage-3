#lamda-namhin function,def keyword er priborte lamda keyword use hoy,argument onek hote pare but expression  1ti hbe
#expression- lamda argument:expression
double=lambda x:x*2
print(double(5))


#local variable(only nijosho kud bloker modde use hoy),glubal variable(jekuno jaygay use kra jay)
x='global'
def foo():
    global x #global keyword use krece bcz global variable declear krece
    y='local'
    print(x*2)
    print(y)
foo()

#non local variable
#local variable k nijer scoper bahireo use korte hoy tokhn nonlocal keyword use koret hoy
print('nonlocal')
def myfunc1():
    x='local variable'
    def myfunc2():
        nonlocal x
        x="local variable change"
    myfunc2()
    return x
print(myfunc1())










