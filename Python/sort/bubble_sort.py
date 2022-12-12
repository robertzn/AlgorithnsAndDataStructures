
print("-----start bubble sort-------")

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                print("Swap happened")
                arr[num], arr[num+1] = arr[num+1], arr[num]
                print(arr)
l = [6,8,1,4,10,7,8,9,3,2,5]
bubble_sort(l)

print("-----end bubble sort-------")
#step 1
#[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
#[6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]



