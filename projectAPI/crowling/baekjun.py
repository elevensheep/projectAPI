a, b = map(int, input().split())
c = int(input())

result = b + c
if(result >= 60 and a < 23):
    a += 1
    if(result == 60):
        result = 0
    else:
        result -= 60
elif(result >= 60 and a == 23):
    a = 0
    if(result == 60):
        result = 0
    else:
        result -= 60

print(a, result)