#!/bin/python

def maxHeapify(heap,heapSize,nodeNumber):
    max = nodeNumber;
    l = 2*nodeNumber+1;
    r = 2*nodeNumber+2;
    # print(max,l,r,heapSize);
    if(l<heapSize and heap[l]>heap[max]):
        max = l;
    if(r<heapSize and  heap[r]>heap[max]):
        max = r;
    if(max!= nodeNumber):
        maxValue=heap[nodeNumber];
        heap[nodeNumber]=heap[max];
        heap[max]=maxValue;
        maxHeapify(heap,heapSize,max);

def intialHeap(heap,heapSize):
    i=int((heapSize-1)/2);
    while(i>=0):
        maxHeapify(heap,heapSize,i);
        i+=-1;

def heapSort(arr):
    # arr = [14,312,123,534,3,56,2346,4157];
    heapSize = len(arr);
    intialHeap(arr,heapSize);
    for i in range(heapSize-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        maxHeapify(arr, i, 0);
    print(arr);

if (__name__ == '__main__'):
    arr = [int(num) for num in input('Enter array for sorting :').strip().split(" ")];
    heapSort(arr);
