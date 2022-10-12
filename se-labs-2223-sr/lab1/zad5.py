def peti():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    zajednicki=[]
 
    for l1 in a:
        for l2 in b:
            if(l1==l2):
                zajednicki.append(l1)
 
    print("Zajednicka lista")
    for number in zajednicki:
        print(number)