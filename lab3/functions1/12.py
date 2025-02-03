def histogram(lst):
    for num in lst:
        print('*' * num)

arr=list(map(int,input().split()))
print(histogram(arr))
