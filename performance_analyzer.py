from random import randint
from demos import quicksort, mergesort, bubblesort, selectionsort, insertionsort
import time

def random_list_generator(list_size, max_range_value):
    return [randint(1, max_range_value) for i in range(list_size)]

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")


print(f"Algorithms file loaded")
list_size = int(input("What size list do you want to create? "))
max_range_value = int(input("What is the max value of the range? "))
no_of_runs = int(input("How many times do you want to run? "))

for num in range(no_of_runs):
    print(f"Run: {num+1}")
    l = random_list_generator(list_size, max_range_value)
    analyze_func(quicksort, l)
    # analyze_func(mergesort, l)
    # analyze_func(bubblesort, l.copy())
    # analyze_func(selectionsort, l.copy())
    # analyze_func(insertionsort, l.copy())
    analyze_func(sorted, l)
    print("-" * 40)
