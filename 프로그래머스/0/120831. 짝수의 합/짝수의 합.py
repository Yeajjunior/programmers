def solution(n):
    k=0
    for i in range(n+1) :
        if i%2 == 0 :
            k+=i
    return k