# input array
arr = [3,4,5,6,7,8,9]
target = 10

l = 0
h = len(arr)-1
result = False
# loop
print('low', l)
while  l  < h:
    #divide
    mid = (l + h)//2 # this is the middele index

    print('mid', mid)
    print('low', l)
    print('high', h)
    print("-----")


# compare the middle with the target
    if arr[mid] == target:
        result == True
        break

    #comapre and discard the half
    if target > arr[mid]:
        l = mid + 1
    else:
        h = mid - 1   

if result == True:
    print('Found')
else:
    print('Not Found')