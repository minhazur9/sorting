def insertion_sort(array):
    size = range(1,len(array))
    for num in size:
        value = array[num]
        while array[num-1] > value and num > 0:
            array[num], array[num-1] = array[num-1], array[num]
            num = num - 1

print(insertion_sort([72 62 17 1 58 11 4 90 56 61 18 33 74 24 36 26 79 21 97 44 49 53 89 77 41 32 38 43 22 28 6 47 45 66 55 35 68 87 94 27 34 14 3 48 15 81 64 46 13 39 91 84 51 92 30 71 86 29 40 96 85 78 9 76 70 59 20 42 23 88 82 50 10 16 99 65 75 8 67 95 7 69 12 31 63 19 52 83 54 80 100 5 60 73 93 25 37 98 57 2]))