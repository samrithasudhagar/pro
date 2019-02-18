n=int(input())
for i in range(100):
    if n==2**i:
        print("0")
        break
    elif n<2**i:
        print(2**i-n)
        break
