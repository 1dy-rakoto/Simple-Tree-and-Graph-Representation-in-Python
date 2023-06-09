"""input:list l,value x 
    output:int n
    searching the index of a value x in a ordered list l
"""
def binarySearch(array:list,x)->int:
    start=0
    end=len(array)
    while start<end:
        mid=(start+end)//2
        if array[mid]<x:
            start=mid+1
        else:
            end=mid
    return start


if __name__=="__main__":
    table=[1,4,5,7,8,9,10,12,15,20]
    print(binarySearch(table,9))
    