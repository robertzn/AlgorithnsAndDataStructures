def merge_sorted(arr1, arr2):
    print("Merge function called with lists below:")
    print(f"left list: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has values: {arr1[i]}")
        # print(f"Right list index j is {j} and has values: {arr1[j]}")
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    while i < len (arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len (arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


l1 = [2,4,6,8,11,17,40]
l2 = [1,3,5,7,8,9,10]
print(f"Merged list: {merge_sorted(l1, l2)}")