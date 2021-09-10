def remove_duplicates(arr):
    if len(arr) < 2:
        return arr
    pre = 0
    for cur in range(1, len(arr)):
        if arr[cur] != arr[pre]:
            pre += 1
            arr[pre] = arr[cur]
    return pre+1, arr[:pre+1]

if __name__ == '__main__':
    arr = [1,2,3,3,3,4,4,5,7,7,7]
    print(remove_duplicates(arr))
    # (6, [1, 2, 3, 4, 5, 7])
            
        
