import random
import time

def sequential_search(alist, item):
    """Simple sequential search through a list"""
    start_time = time.time()
    
    for i in range(len(alist)):
        if alist[i] == item:
            return True, time.time() - start_time
    return False, time.time() - start_time

def ordered_sequential_search(alist, item):
    """Sequential search that stops early if we pass where the item should be"""
    start_time = time.time()
    
    for i in range(len(alist)):
        if alist[i] == item:
            return True, time.time() - start_time
        if alist[i] > item:
            return False, time.time() - start_time
    return False, time.time() - start_time

def binary_search_iterative(alist, item):
    """Binary search using a while loop"""
    start_time = time.time()
    first = 0
    last = len(alist) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True, time.time() - start_time
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False, time.time() - start_time

def binary_search_recursive(alist, item):
    """Binary search using recursion"""
    start_time = time.time()
    
    def recursive_search(first, last):
        if first > last:
            return False
        
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return recursive_search(first, mid - 1)
        else:
            return recursive_search(mid + 1, last)
    
    found = recursive_search(0, len(alist) - 1)
    return found, time.time() - start_time

def main():

    sizes = [500, 1000, 5000]
    
    # We'll search for this number (it won't be in our lists)
    target = 99999999
    

    for size in sizes:
        print(f"\nTesting lists of size {size}")
        
        # Run 100 trials and average the results
        seq_total = ord_total = bin_iter_total = bin_rec_total = 0
        
        for _ in range(100):
            # Make a random list and sort a copy for the ordered/binary searches
            numbers = [random.randint(1, 1000000) for _ in range(size)]
            sorted_numbers = sorted(numbers)
            

            _, seq_time = sequential_search(numbers, target)
            _, ord_time = ordered_sequential_search(sorted_numbers, target)
            _, bin_iter_time = binary_search_iterative(sorted_numbers, target)
            _, bin_rec_time = binary_search_recursive(sorted_numbers, target)
            
            seq_total += seq_time
            ord_total += ord_time
            bin_iter_total += bin_iter_time
            bin_rec_total += bin_rec_time
        

        print(f"Sequential Search took {seq_total/100:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ord_total/100:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {bin_iter_total/100:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {bin_rec_total/100:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
