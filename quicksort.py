def quick(arr):
     size=len(arr)
     if size<=1:
          return arr
     else:
          pivot=arr.pop()
     small=[]
     big=[]
     for element in arr:
          if element>pivot:
               big.append(element)
          else:
               small.append(element)
     return quick(small)+[pivot]+quick(big)
print(quick([3,2,4,1,5]))