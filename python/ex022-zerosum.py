def hasZeroSumSublist(A):
 
    # create an empty set to store the sum of elements of each
    # sublist `A[0…i]`, where `0 <= i < len(A)`
    s = set()
 
    # insert 0 into the set to handle the case when sublist with
    # zero-sum starts from index 0
    s.add(0)
 
    sum = 0
 
    # traverse the given list
    for i in A:
 
        # sum of elements so far
        sum += i
 
        # if the sum is seen before, we have found a sublist with zero-sum
        if sum in s:
          print (s, sum)
          return True
 
        # insert sum so far into the set
        s.add(sum)
        # print (s, sum)
    # we reach here when no sublist with zero-sum exists
    return False
 
 
if __name__ == '__main__':
 
    A = [3, 4, 3, 1, 3, 1, -4, -2, -2, -7]
 
    if hasZeroSumSublist(A):
        print("Sublist exists")
    else:
        print("Sublist does not exist")