### Insertion Sort

#### Psuedocode
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

```

We are given a sample array that we want to sort.

![Screen Shot 2021-06-21 at 4 58 45 PM](https://user-images.githubusercontent.com/45111611/122827685-aa69bc80-d2b2-11eb-9de4-f174f79d9c88.png)

On the first pass we start at index one and while the target number is less then that number to the left we continue to shuffle

![Screen Shot 2021-06-21 at 4 58 48 PM](https://user-images.githubusercontent.com/45111611/122827767-cc633f00-d2b2-11eb-8445-8e369cc7c1ab.png)

Until we get get to the end of the list

![Screen Shot 2021-06-21 at 4 58 51 PM](https://user-images.githubusercontent.com/45111611/122827846-ebfa6780-d2b2-11eb-904c-38a5c0f9fe34.png)

On the next pass we do the same. 8 is less then 20

![Screen Shot 2021-06-21 at 4 58 57 PM](https://user-images.githubusercontent.com/45111611/122827877-f61c6600-d2b2-11eb-9ba5-0d471c2c5f5e.png)

8 is less then 18 and we have reached the end of the list

![Screen Shot 2021-06-21 at 4 59 07 PM](https://user-images.githubusercontent.com/45111611/122827956-0e8c8080-d2b3-11eb-9d62-4bd648401fdc.png)

One more time as an example:
12 is less then 20

![Screen Shot 2021-06-21 at 4 59 11 PM](https://user-images.githubusercontent.com/45111611/122827983-16e4bb80-d2b3-11eb-9e2d-83697a4652a7.png)

12 is less then 18

![Screen Shot 2021-06-21 at 4 59 14 PM](https://user-images.githubusercontent.com/45111611/122828001-1a784280-d2b3-11eb-846b-79ec4f95be46.png)

Becasue 12 is greater then 8 we do not proceed

![Screen Shot 2021-06-21 at 4 59 18 PM](https://user-images.githubusercontent.com/45111611/122828048-25cb6e00-d2b3-11eb-87d1-31df44846094.png)


#### Python Code:

```
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


```

#### Space and Time Complexity:

**Time:** This would be 0(n^2) becasue worst case it has to run the length of the array twice.

**Space:** O(1) because this is happening in place
