#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.

    def heapify(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Check if left child exists and is greater than the largest element.
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        # Check if right child exists and is greater than the largest element.
        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        # Swap the largest element with the current element if necessary and recursively heapify the affected subtree.
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    
    
    def buildHeap(self, arr, n):
        # Start from the last non-leaf node and heapify all nodes.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)

        # Extract elements one by one from the heap and place them at the end of the array.
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum element) with the last element.
            self.heapify(arr, i, 0)  # Heapify the reduced heap.


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends