def merge_2_sorted_lists(L1,L2):
    l1_sz = len(L1)
    l2_sz = len(L2)

    sorted_output = []
    i=0
    j=0

    while i < l1_sz and j < l2_sz:
        if L1[i] < L2[j]:
            sorted_output.append(L1[i])
            i += 1
        else:
            sorted_output.append(L2[j])
            j += 1
    
    sorted_output = sorted_output + L1[i:] + L2[j:]
    return sorted_output

def merge_2_sorted_lists_heapq(L1,L2):
    from heapq import merge
    return list(merge(L1,L2))

if __name__ == '__main__':
    a = [1,2,3,5,6,10,32]
    b = [4,7,25,46]
    print(merge_2_sorted_lists(a,b))
    #[1, 2, 3, 4, 5, 6, 7, 10, 25, 32, 46]
    print(merge_2_sorted_lists_heapq(a,b))
    #[1, 2, 3, 4, 5, 6, 7, 10, 25, 32, 46]
