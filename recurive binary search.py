def BinarySearch(l,low,high,key):
    while low<=high:
         mid=(low+high)//2
         if l[mid]==key:
            return mid
         elif l[mid]<key:
            return BinarySearch(l,mid+1,high,key)
         else:
              return BinarySearch(l,low,mid-1,key)
    return-1
l=[7,8,9,10,15,18]
low=0
n=len(l)-1
key=int(input("enter the searching element:"))
result=BinarySearch(l,low,n,key)
if result==-1:
   print("element not found")
else:
    print("element found:",result)

