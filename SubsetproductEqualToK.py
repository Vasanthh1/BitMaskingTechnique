def countOfSubsetProduct(n,k):
    count = 0
    for i in range(pow(2,n)):
        val = 1
        for j in range(n):
            if i&(1<<j):
                val*=l[j]
                #print(l[j],end=" ")
        if val<k:
            #print("----->",val)
            count +=1
        #print()
    return count-1

if __name__=='__main__':
    l = list(map(int,input().split()))
    n = len(l)
    k = int(input())
    print(countOfSubsetProduct(n,k))
