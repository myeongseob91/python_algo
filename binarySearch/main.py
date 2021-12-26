def location(S, low, high):
    if(low > high):
        return 0
    else:
        mid = (low + high) // 2
        if(x == S[mid]):
            return mid
        elif(x < S[mid]):
            return location(S, low, mid - 1)
        else:
            return location(S, mid + 1, high)


S = [-1, 2, 4, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45]
x = 17
loc = location(S, 1, len(S) - 1)

print('loc =', loc);
