def Insertion (Array):
    if len(Array) > 1:

        for I in range (0, len(Array)):
            Key = Array[I]
        
            K = I
            while (     (K > 0)
                    and (Array[K-1] > Key)):
               Array[K] = Array[K-1]
               K = K - 1 
            Array[K] = Key

    return Array

def Radix (Array):

    NUMBER_OF_PASSES = 4
    NUMBER_OF_BITS_IN_MASK = 8
    NUMBER_OF_BINS = 256
    MASK = 0xFF

    N = len(Array)
    if N <= 1:
        return Array

    for Pass in range (0, NUMBER_OF_PASSES):
        Bin = []
        for I in range (0, NUMBER_OF_BINS):
            Bin.append([])
    
        Shift = Pass * NUMBER_OF_BITS_IN_MASK
    
        for I in range(0, N):
            J = (Array[I] >> Shift) & MASK
            Bin[J].append(Array[I])
 
        I = 0
        if Pass != NUMBER_OF_PASSES - 1:
            for J in range(0, NUMBER_OF_BINS):
                for K in range(0, len(Bin[J])):
                    Array[I] = Bin[J][K]
                    I = I + 1
        else: 
            for J in range(NUMBER_OF_BINS/2, NUMBER_OF_BINS):
                for K in range(0, len(Bin[J])):
                    Array[I] = Bin[J][K]
                    I = I + 1
 
            for J in range(0, NUMBER_OF_BINS/2):
                for K in range(0, len(Bin[J])):
                    Array[I] = Bin[J][K]
                    I = I + 1
    Bin = []
 
    return Array


def Quick (Array, Lower, Upper):

    if (Upper - Lower) <= 1:
        return Array

    Key = Array[(Upper + Lower)/2]

    I = Lower
    J = Upper

    while I <= J:
        while Array[I] < Key:
            I = I + 1

        while Key < Array[J]:
            J = J - 1

        if I <= J:
            Temp = Array[I]
            Array[I] = Array[J]
            Array[J] = Temp
            I = I + 1
            J = J - 1

    if (Upper - I) < (J - Lower):
        if  I < Upper:
            Quick (Array, I, Upper)
    
        if Lower < J:
            Quick (Array, Lower, J)
    else:
        if Lower < J:
            Quick (Array, Lower, J)

        if  I < Upper:
            Quick (Array, I, Upper)
    
    return Array

def Insertion_HT (Array, Head, Tail):
    if len(Array) > 1:
        if Tail - Head > 0:
            for I in range (Head, Tail+1):
                Key = Array[I]
        
                K = I
                while (     (K > Head)
                        and (Array[K-1] > Key)):
                   Array[K] = Array[K-1]
                   K = K - 1 
                Array[K] = Key

    return Array

def Quick_MI (Array, Lower, Upper):
    KK = 8

    if (Upper - Lower) <= 1:
        return Array

    Key = Array[(Upper + Lower)/2]

    I = Lower
    J = Upper

    while I <= J:
        while Array[I] < Key:
            I = I + 1

        while Key < Array[J]:
            J = J - 1

        if I <= J:
            Temp = Array[I]
            Array[I] = Array[J]
            Array[J] = Temp
            I = I + 1
            J = J - 1

    if (Upper - I) < (J - Lower):
        if  I < Upper:
            if (Upper - I + 1) <= KK:
               Insertion_HT (Array, I, Upper)
            else:
               Quick_MI (Array, I, Upper)
    
        if Lower < J:
            if (J - Lower + 1) <= KK:
               Insertion_HT (Array, Lower, J)
            else:
               Quick_MI (Array, Lower, J)
    else:
        if Lower < J:
            if (J - Lower + 1) <= KK:
               Insertion_HT (Array, Lower, J)
            else:
               Quick_MI (Array, Lower, J)

        if  I < Upper:
            if (Upper - I + 1) <= KK:
               Insertion_HT (Array, I, Upper)
            else:
               Quick_MI (Array, I, Upper)
    
    return Array

ROOT = 0
DATA = 0
LEFT = 1
RIGHT = 2

def Tree_Insert (Tree, Value):
    if Tree == []:
        Tree.append([Value, [], []])
    elif Value <= Tree[ROOT][DATA]:
        Tree_Insert (Tree[ROOT][LEFT], Value)
    else:
        Tree_Insert (Tree[ROOT][RIGHT], Value)

    return None

def Tree_Scan (Tree, Sorted):
    if Tree != []:
        Tree_Scan (Tree[ROOT][LEFT], Sorted)

        Sorted.append (Tree[ROOT][DATA])

        Tree_Scan (Tree[ROOT][RIGHT], Sorted)

    return Sorted

def Tree (Array):

    N = len(Array)
    if (N < 2):
        return Array

    Tree = []
    for I in range(0, N):
        Tree_Insert (Tree, Array[I])

    I = 0
    Sorted = []
    Sorted = Tree_Scan (Tree, Sorted)

    return Sorted

def Cook_Kim (Array):
    KK = 8

    N = len(Array)

    if N <= 1:
        return Array

    List = []
    for I in range (0,N):
        List.append (0)
        
    I = -1
    J = 0
    K = N-1
    while J < N:
        # Separate Array into
        # Sorted and Unsorted sections

        if I < 0:
            I = 0
            List[I] = Array[J]
            J = J + 1
        elif List[I] > Array[J]:
            # Place the pair in the
            # Unsorted section

            List[K] = Array[J]
            J = J + 1
            K = K - 1
            List[K] = List[I]
            I = I - 1
            K = K - 1
        else:
            # Place value in sorted section

            I = I + 1
            List[I] = Array[J]
            J = J + 1

    if N -I - 1  > KK:
        Quick_MI (List, I+1, N-1)
    else:
        Insertion_HT (List, I+1, N-1)

    # Merge the sections

    if I < N - 1:
        J = 0
        K = I + 1
        L = 0
   
        while (     (J <= I) \
                and (K < N)):
            if List[J] <= List[K]:
                Array[L] = List[J]
                L = L + 1
                J = J + 1
            else:
                Array[L] = List[K]
                L = L + 1
                K = K + 1
            
        while J <= I:
            Array[L] = List[J]
            L = L + 1
            J = J + 1
 
        while K < N:
            Array[L] = List[K]
            L = L + 1
            K = K + 1
  
    del List
    return Array

