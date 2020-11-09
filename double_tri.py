def triangle():
    n=int(input('How tall: ')) 
    for i in range(n,0, -2):
        if i == 1:
            break
        print ((n-i)*' '+i*'* ')
    for i in range(1,n+1, 2):
        print ((n-i)*' '+i*'* ')
triangle()