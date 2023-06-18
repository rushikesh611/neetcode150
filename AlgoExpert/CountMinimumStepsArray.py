# Input: target[] = {2, 3}
# Output: 4
# To get the target array from {0, 0}, we 
# first increment both elements by 1 (2 
# operations), then double the array (1 
# operation). Finally increment second
# element (1 more operation)

def countMinOperations(target, n):
    result = 0;
    while (True):
        zero_count = 0;
        i = 0;
        while (i < n):
            if ((target[i] & 1) > 0):
                break;
            elif (target[i] == 0):
                zero_count += 1;
            i += 1;
        if (zero_count == n):
            return result;
        if (i == n):
            for j in range(n):
                target[j] = target[j] // 2;
            result += 1;
        for j in range(i, n):
            if (target[j] & 1):
                target[j] -= 1;
                result += 1;