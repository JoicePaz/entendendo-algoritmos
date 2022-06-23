def regressiva(i):
    print i
    if i <= 1:
        retunr
    else:
        regressiva(i-1)


#-------

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)