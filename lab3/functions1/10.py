def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

arr=list(map(int,input().split()))
print(unique_elements(arr))
