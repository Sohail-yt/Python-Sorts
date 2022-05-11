def merge(left,right,small,big):
     result=[]
     small=[]
     big=[]
     i,j=0
     while i<len(left) and j<len(right):
          if left[i]<=right[j]:
               small.append(left[i])
               i+=1
          else:
               big.append(right[j])
               j+=1
     result=[small]+[big]
     return result

def merge(a):
     mid=int(len(a)/2)
     left=merge()
      

a=[1,4,2,3,5]

print(a)

