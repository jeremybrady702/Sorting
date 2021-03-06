# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        cur_val = arr[i]
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i] = arr[smallest_index]
        arr[smallest_index] = cur_val
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    swap_status = True

    while swap_status == True:
        swap_status = False
        # for loop to compare each number
        for i in range(0, len(arr)-1):

            if arr[i] > arr[i+1]:
                left_value = arr[i]
                right_value = arr[i+1]
                arr[i] = right_value
                arr[i+1] = left_value
                swap_status = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
