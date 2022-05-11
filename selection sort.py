def selectionsort(arr):
     for i in range(len(arr)-1): #only loop ye aur -1 aako end tak jaaney key liye agar -1 nai lagaye toh error aataa
          index=i
          for j in range(index+1,len(arr)): #index+1 kato elements ke upper loop,length rakhna to loop for all elements 
               if arr[j]<arr[index]:
                    index=j
          if i!=index:
               arr[i],arr[index]=arr[index],arr[i]                                

if __name__=="__main__":
     arr=[3,5,1,4,2]
     selectionsort(arr)
     print(arr)
