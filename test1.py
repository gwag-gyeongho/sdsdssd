def binary_search(arr, value):
    first, last = 0, len(arr)

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
d=[1,2,3,5,6,7,8,9]
print(binary_search(d,3))