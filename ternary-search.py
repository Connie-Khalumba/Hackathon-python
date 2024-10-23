def ternary_search(low,high,arr,element):
    middle1 = low + (high-low) // 3
    middle2 = high - (high-low) // 3

    if arr[middle1] == element:
        return f'Element found at index {middle1}'
    if arr[middle2] == element:
        return f'Element found at index {middle2}'
    if element < arr[middle1]:
        return ternary_search(low, middle1-1, arr, element) 
    
    elif element > arr[middle2]:
        return ternary_search(middle2+1, high, arr, element)
    
    else:
        return ternary_search(middle1+1, middle2-1, arr, element)

arr = [10,20,55,100,1000]
print(ternary_search(0,len(arr)-1,arr,55))