def rotate(S, O):
    if O == 0:
        return S
    elif O == 1:
        return int(((S%2)*(S+1)+(1-(S%2))*(1-(S/2))))
    else: 
        return int((1-(S%2))*(2-(S/2)))

def inequality_full(T):
    if bool(T[0][1]*T[0][2]*T[0][3]):
        return (T[2][1] + T[2][2] > T[2][3]) and (T[2][1] + T[2][3] > T[2][2]) and (T[2][2] + T[2][3] > T[2][1])

def paradigm3_check(T):
    if bool(T[0][2]*T[0][3]*T[0][4]):
        T[3][2] = 0
        return True
    if bool(T[0][1]*T[0][3]*T[0][5]):
        T[3][2] = 1
        return True
    if bool(T[0][1]*T[0][2]*T[0][6]):
        T[3][2] = 2
        return True


def inspect(T):
    defined = False
    if (not defined) and (bool(T[0][0]*T[0][1])):
        if T[2][0]>0 and T[2][1]>0:
            T[3][1] = 1
            T[3][0] = True
            defined = True
    elif (not defined) and (bool(T[0][1]*T[0][2]*T[0][3])):
        if inequality_full(T):
            T[3][1] = 2
            T[3][0] = True
            defined = True
    elif (not defined) and (paradigm3_check(T)):
        #
        print("Ciao") #will be implemented later