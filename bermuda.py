def rotate(O, S): # (OBJECT -> eg????[L1, L2, A0], SHIFT -> T[3][2])
    if O == 0:
        return S
    elif O == 1:
        return int(((S%2)*(S+1)+(1-(S%2))*(1-(S/2))))
    else: 
        return int((1-(S%2))*(2-(S/2)))

def paradigm2_check(T):
    if bool(T[0][1]*T[0][2]*T[0][3]):
        return (T[2][1] + T[2][2] > T[2][3]) and (T[2][1] + T[2][3] > T[2][2]) and (T[2][2] + T[2][3] > T[2][1])

def paradigm3_check(T):
    if bool(T[0][2]*T[0][3]*T[0][4]):
        if (T[2][2] > 0 and T[2][3] > 0 and (0<T[2][4]<180)):
            T[3][2] = 0 
            return True
    if bool(T[0][1]*T[0][3]*T[0][5]):
        if (T[2][1] > 0 and T[2][3] > 0 and (0<T[2][5]<180)):
            T[3][2] = 1
            return True
    if bool(T[0][1]*T[0][2]*T[0][6]):
        if (T[2][1] > 0 and T[2][2] > 0 and (0<T[2][6]<180)):
            T[3][2] = 2
            return True
    return False

def paradigm4_check(T):
    if bool(T[0][2]*T[0][3]*T[0][5]*T[0][6]):
        if ((T[2][2]>0 and T[2][3]>0 and (0<T[2][5]<180) and (0<T[2][6]<180))
        and (T[2][5]+T[2][6]<180)):
            T[3][2] = 0 
            return True
    if bool(T[0][1]*T[0][3]*T[0][4]*T[0][6]):
        if ((T[2][1]>0 and T[2][3]>0 and (0<T[2][4]<180) and (0<T[2][6]<180))
            and (T[2][4]+T[2][6]<180)):
            T[3][2] = 1 
            return True
    if bool(T[0][1]*T[0][2]*T[0][4]*T[0][5]):
        if ((T[2][1]>0 and T[2][2]>0 and (0<T[2][4]<180) and (0<T[2][5]<180))
            and (T[2][4]+T[2][5]<180)):
            T[3][2] = 2 
            return True
    return False    

def paradigm5_check(T):
    return True ### da implementare


def inspect(T):
    defined = False
    if (not defined) and (bool(T[0][0]*T[0][1])):
        if T[2][0]>0 and T[2][1]>0:
            T[3][1] = 1
            T[3][0] = True
            defined = True
    elif (not defined) and (paradigm2_check(T)):
        T[3][1] = 2
        T[3][0] = True
        defined = True
    elif (not defined) and (paradigm3_check(T)):
        T[3][1] = 3
        T[3][0] = True
        defined = True
    elif (not defined) and (paradigm4_check(T)):
        T[3][1] = 4
        T[3][0] = True
        defined = True
    elif (not defined) and (paradigm5_check(T)):
        T[3][1] = 4
        T[3][0] = True
        defined = True                    