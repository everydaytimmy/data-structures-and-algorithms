def merge_sort(list):
    n = len(list)
    if n <= 1:
        return list

    if n > 1:
        mid = n//2
        left = list[0:mid]
        right = list[mid:n]
        merge_sort(left)
        merge_sort(right)
        return merge(left,right,list)

def merge(left, right, list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i = i+1
        else:
            list[k] = right[j]
            j = j+1

        k = k+1

    if i == len(left):
        list[k:] = right[j:]
    else:
        list[k:] = left[i:]
    return list
