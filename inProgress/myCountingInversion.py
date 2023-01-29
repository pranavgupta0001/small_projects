#%%
def mergeSort(array):
    if(len(array)==1):
        return array, 0
    else:
        mid = len(array)//2
        arrayL, nL= mergeSort(array[:mid])
        arrayR , nR= mergeSort(array[mid:])
        
        arrayF = []
        indexL = indexR = 0
        n= nL+nR

        while indexL<len(arrayL) and indexR<len(arrayR) :
            if(arrayL[indexL]<arrayR[indexR]):
                arrayF.append(arrayL[indexL])
                indexL+=1
            else:
                arrayF.append(arrayR[indexR])
                indexR+=1
                n+= len(arrayL)-indexL
               

        arrayF+=arrayL[indexL:]
        arrayF+=arrayR[indexR:]
            
        
        return arrayF, n



mergeSort([1, 20, 6, 4, 5])
