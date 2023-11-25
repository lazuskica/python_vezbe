
print("unutar fajla uvod.py")

if __name__ == "__main__":

    #print("pozdrav")

    #if 5 > 10:
    #    print("manje")
    
    # Tipovi u pythonu

    # string
    """
        string je konstanta
    """
    my_string = "Pozdrav"
    my_message1 = "Broj poena: {}, ocena {}".format(51,6)
    my_message1 = f"Broj poena: {51}, ocena {6}"            # ovo je bolje

    # int
    my_int = 10
    # float
    my_float = 10.0

    # list
    my_list = [10, 2, 13, -1, "string", [1, 2, 3], "aaaaaaa", "bbbbb"]          # ovako se ne radi, iako moze

    # slicing
    start = 0
    end = 3
    step = 1
    print(my_list[start:end:step])

    my_matrix = [
        [1,2,3],
        [4,5,6]
    ]

    print(my_matrix[1][:2])

    # slicing od nazad

    print(my_list[-5:-2])   # 5. od kraja do 2. od kraja

    # FOR petlja
    n = 10
    start = 0
    stop = 10
    step = 2
    # for i in range(n):
    # for i in range(start, stop, step):
    #     print(i)
    
    broj_elemenata = len(my_list)
    # for i in range(broj_elemenata):
    #     print(my_list[i])

    #ili
    print("_________________")
    for element in my_list:
        print(element)

    # while petlja

    # while broj_elemenata < 10:
    #    print("sta god")
    
    uslov = 0
    if uslov:
        print (1)
    elif uslov ==0:
        print ("pusigaubulju")
    else:
        print ("aaa")

    #TIP TUPLE, ne moze da se modifikuje
    my_tuple = (1, 2, 3)
