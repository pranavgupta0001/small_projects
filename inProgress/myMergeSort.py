
#%%
def mergeSort(array):
    if(len(array)==1):
        return array
    else:
        mid = len(array)//2
       
        arrayL= mergeSort(array[mid:])
        
        arrayR= mergeSort(array[:mid])
        

        arrayF = []
        indexL =  0
        indexR = 0
        index = 0

        while indexL<len(arrayL) and indexR<len(arrayR) :
            if(arrayL[indexL]<arrayR[indexR]):
                
                array[index] = arrayL[indexL]
                indexL+=1
            else:
                
                array[index] = arrayR[indexR]
                indexR+=1
            print(arrayL,arrayR, index , indexL, indexR)
            index+=1
        
        while indexL<len(arrayL):
            array[index] = arrayL[indexL]
            indexL+=1
            index+=1

        while indexR<len(arrayR):
            array[index] = arrayR[indexR]
            indexR+=1
            index+=1

            
        
        return array



mergeSort([1, 3, 5, 2, 4, 6])


