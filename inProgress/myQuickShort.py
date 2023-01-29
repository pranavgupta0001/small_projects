

#%%
recursion=0

def quickSort(array):
    if len(array)<=1:
        return array
    
    i = 1
    global recursion
    recursion+= (len(array)-1)
    for x in range(i, len(array)):
        if array[x]<array[0]:
            temp = array[x]
            array[x]= array[i]
            array[i]= temp
            i+=1

    
    return quickSort(array[1:i]) + [array[0]] + quickSort(array[i:])



#print(quickSort([2,1]))
print(quickSort([10, 7, 8, 9, 1, 5] ))
print(recursion)
# %%
arr =[1]
def first(arr):
    arr.append(2)
    second(arr)

def second(arr):
    arr.append(3)

first(arr)
print(arr)

