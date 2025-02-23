import random
import time

def insertion_sort(alist):
    """Sort a list using insertion sort"""
    start_time = time.time()
    
    for index in range(1, len(alist)):
        current = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > current:
            alist[position] = alist[position-1]
            position = position - 1
        
        alist[position] = current
    
    return alist, time.time() - start_time

def shell_sort(alist):
    """Sort a list using shell sort"""
    start_time = time.time()
    gap = len(alist) // 2
    
    while gap > 0:
        for start in range(gap):
            # Do insertion sort with gap
            for i in range(start + gap, len(alist), gap):
                current = alist[i]
                position = i
                
                while position >= gap and alist[position-gap] > current:
                    alist[position] = alist[position-gap]
                    position = position - gap
                
                alist[position] = current
        gap = gap // 2
    
    return alist, time.time() - start_time

def python_sort(alist):
    """Use Python's built-in sort"""
    start_time = time.time()
    alist.sort()
    return alist, time.time() - start_time

def main():
    # List sizes to test
    sizes = [500, 1000, 5000]
    
    # Test each size
    for size in sizes:
        print(f"\nTesting lists of size {size}")
        
        # Run 100 trials and average the results
        insertion_total = shell_total = python_total = 0
        
        for _ in range(100):
            # Make three copies of the same random list
            numbers = [random.randint(1, 1000000) for _ in range(size)]
            numbers1 = numbers.copy()
            numbers2 = numbers.copy()
            numbers3 = numbers.copy()
            
            # Time each sort
            _, insertion_time = insertion_sort(numbers1)
            _, shell_time = shell_sort(numbers2)
            _, python_time = python_sort(numbers3)
            
            insertion_total += insertion_time
            shell_total += shell_time
            python_total += python_time
        
        # Print average times
        print(f"Insertion Sort took {insertion_total/100:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_total/100:10.7f} seconds to run, on average")
        print(f"Python Sort took {python_total/100:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
