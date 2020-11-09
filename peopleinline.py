
list_tiket_avengers = [25, 25, 25, 50, 100]

def ticket(list_tiket):
    kembalian = False
    list_25 = []
    list_50 = []
    list_kembalian_50 = []
    list_kembalian_100 = []
    for tiket in list_tiket:
        if tiket == 25:
            list_25.append(25)
        elif tiket == 50:
            list_kembalian_50.append(25)
            if sum(list_kembalian_50) <= sum(list_25):
                list_25.remove(25)                                        
                list_50.append(50)
            else:                
                 kembalian = True
                 break                                       
        else:
            list_kembalian_100.append(75)           
            if sum(list_kembalian_100) <= sum(list_25) + sum(list_50) and sum(list_50) != 0:               
                list_25.remove(25)
                list_50.remove(50)
            elif sum(list_kembalian_100) <= sum(list_25):
                del list_25[0:3]           
            else:                
                kembalian = True
                break 

    if kembalian == True:
        print("No, Vasya does not have enough change")
    else:
        print("Yes, Vasya has enough change") 
    print(list_25)
    print(list_50)
    print(list_kembalian_50)
    print(list_kembalian_100)
ticket(list_tiket_avengers)  



