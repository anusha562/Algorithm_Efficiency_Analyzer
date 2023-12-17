import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import time
import matplotlib.pyplot as plt
import re

# Sorting algorithms
# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr     
       
# Linear Sorting (Counting Sort)
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# heap Sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Linear sorting : radix sort
def radix_sort(arr):

    itr = False
    exp = 1
    while not itr:
        # create buckets of 10 decimals
        buckets = [[] for _ in range(10)]        
        itr = True 
        for i in arr:
            num_digit = i % (exp*10) // exp
            buckets[num_digit].append(i)
            if i >= exp*10:
                itr = False

        arr = [i for j in buckets for i in j]
        exp *= 10
    return arr

# Quick Sort        
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for i in range(bucket_count):
    # Convert index to an integer
        idx = int((arr[i] - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[idx].append(arr[i])
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])
    
    return [val for sublist in buckets for val in sublist]


#This function checks if the input contains alphabets, alphanumeric or any special characters and gives appropriate error message
def show_popup(input):
    if re.match('[A-Za-z ]+$', input):
        tk.messagebox.showerror('Error!','Alphabets detected!\nOnly numbers are allowed')
    elif re.match('[\w\d ]*$', input):
        tk.messagebox.showerror('Error!','Alphanumeric characters detected!\nOnly numbers are allowed')  
    else:
        tk.messagebox.showerror('Error!','Special characters detected!\nOnly numbers are allowed')
        
#This function shows the sorted array and the selected algorithm as a pop-up window
def show_sorted(selected_algo, input):
    tk.messagebox.showinfo(selected_algo, input)

# This function adds labels to the graphs 
def graphlabels(algo, totaltimes):
    for i in range(len(algo)):
        plt.text(i, totaltimes[i], f"{totaltimes[i]:.2e}", ha='center', va='bottom', fontsize=10)
                    
def analyze_efficiency():
    # Retrieve the selected algorithm and input data from the GUI
    selected_algorithm = algos.get()
    input_data = input_data_entry.get()
    selected_graph = graphs.get()
    
    #This regex expression validates the input containing numbers
    if re.match('^[-\d ]*$', input_data):
        inputs = [int(x) for x in input_data.split()]        
         
        # Perform the analysis and display the results or graphs as needed
        # You can implement the analysis logic here
        algorithms = ["Bubble Sort", "Counting Sort", "Radix Sort", "Bucket Sort", "Insertion Sort",
                    "Merge Sort", "Heap Sort", "Quick Sort"]
        times = []
        
        #Checks if the user input is less than 2
        if len(inputs) < 2:
            tk.messagebox.showerror('Error!', 'Please enter more than one number')
            
        else:     
            for algorithm in algorithms:
                # print("Algorithm:", algorithm)
                algorithm_time = 0.0
                for iteration in range(12):
                    data = inputs[:]
                    if algorithm == "Bubble Sort":
                        start_time = time.perf_counter()
                        bubble_sort(data)
                        elapsed_time = time.perf_counter() - start_time    
                    elif algorithm == "Counting Sort":
                        start_time = time.perf_counter()
                        counting_sort(data)
                    elif algorithm == "Radix Sort":
                        start_time = time.perf_counter()
                        radix_sort(data)
                        elapsed_time = time.perf_counter() - start_time
                    elif algorithm == "Bucket Sort":
                        start_time = time.perf_counter()
                        bucket_sort(data)
                        elapsed_time = time.perf_counter() - start_time
                    elif algorithm == "Insertion Sort":
                        start_time = time.perf_counter()
                        insertion_sort(data)
                        elapsed_time = time.perf_counter() - start_time
                    elif algorithm == "Merge Sort":
                        start_time = time.perf_counter()
                        merge_sort(data)
                        elapsed_time = time.perf_counter() - start_time
                    elif algorithm == "Heap Sort":
                        start_time = time.perf_counter()
                        heap_sort(data)
                        elapsed_time = time.perf_counter() - start_time
                    elif algorithm == "Quick Sort":
                        start_time = time.perf_counter()
                        quicksort(data)
                        elapsed_time = time.perf_counter() - start_time
                    
                    algorithm_time += elapsed_time

                average_time = algorithm_time / 12  #Calculate the average time
                times.append(average_time)
        
             #Checks if the input is already sorted or not using python's in-built sorted function    
            
            if inputs == sorted(inputs):            
                tk.messagebox.showinfo('Already sorted', 'Data is already sorted')
                
            else:
                algorithms = ["Bubble Sort", "Insertion Sort", "Counting Sort", "Radix Sort", "Bucket Sort", 
                    "Merge Sort", "Heap Sort", "Quick Sort"]
                
                if selected_algorithm == "All" and selected_graph == "Bar Graph":
                    show_sorted(selected_algorithm, bubble_sort(inputs))
                    plt.figure(figsize=(10, 6))
                    plt.bar(algorithms, times, color='skyblue', width=0.45)
                    plt.ylabel("Average Time (s)")
                    plt.xlabel("Sorting Algorithms")
                    plt.title("Algorithm Efficiency Analysis")
                    graphlabels(algorithms, times)
                    plt.show()

                if selected_algorithm == "All" and selected_graph == "Scatterplot":
                    show_sorted(selected_algorithm, bubble_sort(inputs))
                    plt.figure(figsize=(10, 6))
                    plt.scatter(algorithms, times, color='yellow', marker='o')
                    plt.xlabel("Sorting Algorithms")
                    plt.ylabel("Average Time (s)")
                    plt.title("Algorithm Efficiency Analysis")
                    plt.xticks(rotation=15)
                    plt.grid(True)
                    graphlabels(algorithms, times)
                    plt.show()
                
                if selected_algorithm == "All" and selected_graph == "None":
                    tk.messagebox.showinfo('Error!', 'Select a graph!')
                    
                if selected_algorithm == "Bubble Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, bubble_sort(inputs))
                    
                if selected_algorithm == "Counting Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, counting_sort(inputs))
                
                if selected_algorithm == "Radix Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, radix_sort(inputs))
                
                if selected_algorithm == "Bucket Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, bucket_sort(inputs))
                    
                if selected_algorithm == "Insertion Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, insertion_sort(inputs))
                    
                if selected_algorithm == "Merge Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, merge_sort(inputs))
                    
                if selected_algorithm == "Heap Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, heap_sort(inputs))
                    
                if selected_algorithm == "Quick Sort" and selected_graph == "None":
                    show_sorted(selected_algorithm, quicksort(inputs))
                
                if selected_algorithm in algorithms and selected_graph == "Bar Graph":
                    tk.messagebox.showinfo('Error!', 'Put graph on None!')
                
                if selected_algorithm in algorithms and selected_graph == "Scatterplot":
                    tk.messagebox.showinfo('Error!', 'Put graph on None!')

    else:
        show_popup(input_data)
    
    
    # For demonstration purposes, let's just print the selected algorithm and input data
    print("Selected Algorithm:", selected_algorithm)
    print("Input Data:", input_data)
    print("Selected Graph", selected_graph)

root = Tk()
root.title("Algorithms Efficiency Analyzer")
root.minsize(600, 700)
root.resizable(0,0)
ttk.Label(root, text="Algorithms Efficiency Analyzer").grid(column=8, row=3)
ttk.Label(root, text="").grid(column=8, row=4)

#Algorithms selection
ttk.Label(root, text="Select the Algorithms:").grid(column=8, row=5)
algos = tk.StringVar()
selectalgos = ttk.Combobox(root, width=54, textvariable=algos)
selectalgos['values'] = ('All',
                        'Bubble Sort',
                        'Counting Sort',
                        'Radix Sort',
                        'Bucket Sort',
                        'Insertion Sort',
                        'Merge Sort',
                        'Heap Sort',
                        'Quick Sort')
selectalgos.grid(column=8, row=6)
selectalgos.current(0)

#Input data
ttk.Label(root, text="").grid(column=8, row=7)
ttk.Label(root, text="Enter Input Data (with whitespace):").grid(column=8, row=8)

input_data = tk.StringVar()
input_data_entry = ttk.Entry(root, width=60, textvariable=input_data)
input_data_entry.grid(column=8, row=9)

#Select graphs
ttk.Label(root, text="").grid(column=8, row=10)
ttk.Label(root, text="Select Graphs:").grid(column=8, row=11)
graphs = tk.StringVar()
selectgraphs = ttk.Combobox(root, width=54, textvariable=graphs)
selectgraphs['values'] = ('None',
                          'Bar Graph',
                          'Scatterplot'
                          )
selectgraphs.grid(column=8, row=12)
selectgraphs.current(0)

selectgraphs.grid(column=8, row=13)

ttk.Label(root, text="").grid(column=8, row=14)
analyze_button = ttk.Button(root, text="Analyze", command=analyze_efficiency)
analyze_button.grid(column=8, row=15)

root.mainloop()
