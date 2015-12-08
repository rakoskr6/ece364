#   $Author: ee364 $
#     $Date: 2001/03/26 19:12:21 $
# $Revision: 1.4 $

import copy

def Intersection(List_1, List_2):

    # Returns a shallow copy the intersection
    # of List_1 and List_2

    Result = []
    for Item in List_1:
        if Item in List_2:
            Result.append(Item)
    return Result

def Union(List_1, List_2):

    # Returns a shallow copy the union
    # of List_1 and List_2

    Result = list(List_1)
    for Item in List_2:
        if not Item in Result:
            Result.append(Item)
    return Result

def Intersection_DC(List_1, List_2):

    # Returns a deep copy the intersection
    # of List_1 and List_2

    Result = []
    for Item in List_1:
        if Item in List_2:
            Result.append(Item)
    return copy.deepcopy(Result)

def Union_DC(List_1, List_2):

    # Returns a deep copy the union
    # of List_1 and List_2

    Result = list(List_1)
    for Item in List_2:
        if not Item in Result:
            Result.append(Item)
    return copy.deepcopy(Result)
