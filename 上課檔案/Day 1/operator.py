'''
運算子 Operator: 
    (1)數學運算 num op num -> num 
        1.取餘數 %
        2.取商數 //
        3.指數 **
        eg.
            print(20%3)
            print(20//3)
            print(3**2)
    
    (2)邏輯運算 
        [1] num op num -> bool 
            1. <,>,>=(> or ==),<=(< or ==)
            2. ==(equal), !=(not equal)
            eg.
                print(1 < 2)
        
        [2]bool op bool -> bool (Logic Gates)
            1.not 反閘
                周杰倫：哎呦不錯喔 -> True
                不(not)錯(False) -> True
                錯 -> False
                不(not)行(True) -> False
                行 -> True
                eg.
                    a = False
                    print(not a)
            2.or 或閘
                期中考60 或 期末考60 -> pass
                T.         F.         T
                F.         T.         T
                T.         T.         T
                F.         F.         F
                eg.
                    a, b = False, False
                    print(a or b)
            3.and 且閘
                Homework and Report -> pass
                T.           F.        F
                F.           T.        F
                T.           T.        T
                F.           F.        F
                eg.
                    a, b = False, False
                    print(a and b)
            4.xor(excursive or) 斥或閘
                珍奶 xor 烏龍拿鐵 -> :)
                T.       F.        T
                F.       T.        T
                T.       T.        F
                F.       F.        F
                [1] not, or, and
                    a, b = False, False
                    print((a or b) and not(a and b))
                [2] bin
                    a, b = False, False
                    print(a ^ b)

    運算元 Operatee
'''

a = 1
# a(new) = a(old) + 1
a += 1








