def hana(n, pin_1, pin_2, pin_3):
    if n <= 0: 
        return
    hana(n-1, pin_1, pin_3, pin_2)
    print("Переместить диск ", n, " со штырька ", pin_1, " на штырек ", pin_3)
    hana(n-1, pin_2, pin_1, pin_3)

hana(5, "A", "B", "C")