'''
*문제

:첫째 줄에 N의 약수들 중 K번쨰로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 작아서
K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
'''
import sys
sys.stdin=open("input.txt","rt")
n, k=map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
