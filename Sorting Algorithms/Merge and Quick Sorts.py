#merge sort and quick sort 

def mergeSort(arr):
    #Stopping the recursion part
    if(len(arr) == 1):
        #the spliting process already broke the array into a 1-element-sorted state
        return
    #Split the array part
    mid = int(len(arr)//2)
    left = arr[0:mid]
    right = arr[mid:int(len(arr))]

    #Recursive break down the size of the array part
    mergeSort(left)
    mergeSort(right)
    
    #Merge the array part
    merge(arr, left, right)
    
#O(n) for the merging process
def merge(arr, left, right):
    i = 0
    k = 0
    t = 0
    while(i< len(left) and k < len(right)):
        if(left[i] < right[k]):
            arr[t] = left[i]
            t+=1
            i+=1
        else:
            arr[t] = right[k]
            t+=1
            k+=1
    while(i < len(left)):
        arr[t] = left[i]
        t+=1
        i+=1
    while(k < len(right)):
        arr[t] = right[k]
        t+=1
        k+=1
        
#The pivot is always the last index in the array in my version
def quickSort(arr, start, end):
    
    #Stopping the recursion part
    if end <= start:
        return
    
    leftPointer = start;
    rightPointer = end;
    pivot = end;
    
    #partitioning part
    while(leftPointer < rightPointer):
        
        while(arr[leftPointer] <= arr[pivot] and leftPointer < rightPointer):
            leftPointer+=1;
            
        while(arr[rightPointer] >= arr[pivot] and leftPointer < rightPointer):
            rightPointer-=1;
            
        temp = arr[leftPointer]
        arr[leftPointer] = arr[rightPointer]
        arr[rightPointer] = temp
    
    #Swap the left pointer and pivot's positions
    temp = arr[pivot]
    arr[pivot] = arr[leftPointer]
    arr[leftPointer] = temp;
    
    quickSort(arr, start, leftPointer - 1);
    quickSort(arr, leftPointer, end);