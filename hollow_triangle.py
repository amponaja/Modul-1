def hollowTriangel(angka) :

    if type(angka) != int :
        return 'Just input number'
    else :
        bintang = ''
        for a in range(0,angka) :
            if a == angka-1 :
                bintang += '#'*(angka*2-1)
            elif a == 0 :
                bintang += '_'*(angka-a-1) + '#' + '_'*(angka-a-1) + '\n'
            else :
                bintang += '_'*(angka-a-1) + '#' + '_'*(a*2-1) + '#' + '_'*(angka-a-1) + '\n'

        return bintang

print(hollowTriangel(6))