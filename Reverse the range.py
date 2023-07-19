def reverse_range(arr,begin,end):
    while(end>begin):
        arr[begin],arr[end]=arr[end],arr[begin]
        begin+=1
        end-=1
    return arr
x=list(map(int,input().split()))
y,z = map(int,input().split())
print(reverse_range(x,y,z))
