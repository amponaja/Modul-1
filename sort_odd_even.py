def sort_odd_even(num) :

    odd = []
    even = []
    for a in range(0,len(num)) :
        if num[a]%2 == 0 :
            even.append(a)
        else :
            odd.append(a)
    for a in range(0,len(odd)-1) :
        for b in range(a,len(odd)) :
            if num[odd[a]] > num[odd[b]] :
                num[odd[a]], num[odd[b]] = num[odd[b]], num[odd[a]]

    for a in range(0,len(even)-1) :
        for b in range(a,len(even)) :
            if num[even[a]] < num[even[b]] :
                num[even[a]], num[even[b]] = num[even[b]], num[even[a]]

    return num

print(sort_odd_even([5,3,2,8,1,4]))
print(sort_odd_even([5,7,2,8,1,4,3,6,9]))