def prime(n):
    count=0
    if n>1:
        for i in range(1,n+1):
            if(n%i)==0:
                count +=1
        if count==2:
            return True
        else:
            return False

def sum(n):
    sum=0
    while n>0:
        digit=n%10
        digit=sum+digit
        n=n//10
    return sum

def additiveprime(n):
    if (not prime(n)):
        return False
    else:
        return True
  
    # return prime(sum(n))
print(additiveprime(98))