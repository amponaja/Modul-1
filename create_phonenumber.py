def create_phone_number(number) :
    angka = 0
    x = 0
    for a in number :
        if type(a) == int :
            angka += 1
        if a > 9 or a < 0  :
            x += 1


    if angka != len(number) :
        return 'Just input the number'
    elif x != 0 :
        return 'Just input number in range 0-9'
    elif len(number) == 10 :
        no = '('
        for a in range(0,3) :
            no += str(number[a])
        no += ') '
        for a in range(3,6) :
            no += str(number[a])
        no += '-'
        for a in range(6,len(number)) :
            no += str(number[a])        
        return no
    else :
        return 'Input 10 digits of number!'

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))