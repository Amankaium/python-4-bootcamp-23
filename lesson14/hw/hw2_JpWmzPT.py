def f_hanoi(n, A, C):
    if n <= 0 :
        return
    B = 6 - A - C
    f_hanoi(n - 1, A, B)
    print(f"Переместить диск {n} со штырька {A} на штырек {C}")
    f_hanoi(n - 1, B, C)
f_hanoi(5,1,3)