import numpy as np
import matplotlib.pyplot as plt
import time

def q(a3,a2,a1,a0,t):
    return a3*t**3 + a2*t**2 + a1*t + a0

def q_prim(a3,a2,a1,a0,t):
    return 3*a3*t**2 + 2*a2*t + a1

def sinteza(a,b,c,d,T):

    A = np.array(
        [
            [T**3, T**2],
            [3*T**2, 2*T]
        ]
    )

    B = np.array([b - (c*T + a), d - c]).T

    x = np.linalg.inv(A) @ B

    a0 = a
    a1 = c
    a2 = x[1]
    a3 = x[0]

    return a0,a1,a2,a3

if __name__ == "__main__":

    q0 = 0
    qT = 0.5
    q0_prim = 0
    qT_prim = 0
    T = 2
    dt = 0.01

    max_velocity = 0.2

    T_min = 0.5
    T_max = 10

    start = time.time()

    for T in np.arange(T_min, T_max + dt, dt):
        a0, a1, a2, a3 = sinteza(q0,qT,q0_prim,qT_prim, T)
        dt_array = np.arange(start = 0, stop = T, step = dt)
        q_t_prim = np.polynomial.Polynomial((a1,2*a2,3*a3))

        if np.max(q_t_prim(dt_array)) < max_velocity:
            q_t = np.polynomial.Polynomial((a0,a1,a2,a3))
            # q_t_prim = np.polynomial.Polynomial((a1,2*a2,3*a3))
            q_t_array = q_t(dt_array)
            q_t_prim_array = q_t_prim(dt_array)
            break



    # a0, a1, a2, a3 = sinteza(q0,qT,q0_prim,qT_prim, T)
    # dt_array = np.arange(start = 0, stop = T+dt, step = dt)
    # ubrzaj tako sto ces da izbacis nasu funkciju
    # q_t_array = q(a3,a2,a1,a0,dt_array)
    # q_t_prim_array = q(a3,a2,a1,a0,dt_array)
    # q_t = np.polynomial.Polynomial((a0,a1,a2,a3))
    # q_t_prim = np.polynomial.Polynomial((a1,2*a2,3*a3))
    # q_t_array = q_t(dt_array)
    # q_t_prim_array = q_t_prim(dt_array)

    # for t in dt_array:
    #     q_t = q(a3,a2,a1,a0,t)
    #     q_t_prim = q_prim(a3,a2,a1,a0,t)

    #     q_t_array.append(q_t)
    #     q_t_prim_array.append(q_t_prim)

    end = time.time()

    print(f"Potrebno vreme je {end - start}")
    print(f"Frekvencija je {1 / (end - start)}")
    
    plt.plot(dt_array, q_t_array)
    plt.plot(dt_array, q_t_prim_array)
    plt.show()