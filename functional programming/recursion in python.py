#nijer kaj nije koro, function er modde function call
def factorial(n):
    print('factorial function has been called with n=' +str(n))
    if n==1:
        return 1
    else:
        result=n*factorial(n-1)
        return result
print('final result %s' %factorial(5))
