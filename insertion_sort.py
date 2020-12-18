import time
start_time = time.time()
def insertion_sort(array):
    size = range(1,len(array))
    for num in size:
        value = array[num]
        while array[num-1] > value and num > 0:
            array[num], array[num-1] = array[num-1], array[num]
            num = num - 1
    return array
    
print("--- %s seconds ---" % (time.time() - start_time))