# Time complexity: O(N^2)
# Space Complexity: O(1)

def find3Numbers(A, arr_size, sum):
    A.sort()
    for i in range(0, arr_size-2):
        l = i + 1
        r = arr_size-1
        while (l < r):
            if( A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i],
                     ', ', A[l], ', ', A[r]);
                return True
             
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1
    # If we reach here, then
    # no triplet was found
    return False