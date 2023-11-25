import numpy as np
import matplotlib.pyplot as plt

def polinom(spisak_koeficijenata):
    """
    args: lista koeficijenata
    return: zapis polinoma kao string: a3*t^3 + a2*t^ + ... + a0
    """
    msg = "q(t) = "
    l = len(spisak_koeficijenata)
    for i in range(1,l,1):
        if spisak_koeficijenata[l-i] != 0:
            msg += f"{spisak_koeficijenata[l-i]}*t^{l-i} + "
    msg += str(spisak_koeficijenata[0])
    print(msg)

    

if __name__ == "__main__":

    niz_nula = np.zeros(3, dtype=np.uint8)
    niz_jedinica = np.ones(3)

    my_list = [1,2,3,4,5,6,7,8,9]
    my_array = np.array(my_list)

    my_matrix = (
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    )
    # print(my_matrix[2,1])
    
    start = 2
    stop = start + 10
    step = 1

    # rampa = list(range(start,stop,step))

    #x_list = list(range(0, 628, 1))
    x_list = np.arange(start=0,stop=2*np.pi, step=0.1)

    def f(x):
        return np.sin(x)
    
    # y_list = [f(x) for x in x_list]
    y_list = np.sin(x_list)

    # plt.plot(x_list, y_list)
    # plt.scatter (x_list, y_list)
    # plt.show()

    polinom([1,0,0,0,6])
