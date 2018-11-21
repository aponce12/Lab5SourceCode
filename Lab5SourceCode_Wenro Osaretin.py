# -*- coding: utf-8 -*-
"""
Course: CS 2302
Author: Wenro Osaretin
Instructor: Diego Aguirre
T.A.: Anindita Nath
Date of Last Modication: November 27, 2018
"""
#This is the Heap Class where I test some numbers in order to insert them,
# extract min out of them, and check if the list is empty.
class Heap:
    #This is where I initialize the array and the size of the heap
    def __init__(self):
        self.heap_array = [0]
        self.size = 0
        
    #This is where I insert the numbers in the heap by adding it in the array,
    # increase the size by one, and then I heapify up by swapping the parent 
    # and the child if the parent is greater than the child while I check if 
    # the index of the parent is greater than zero.
    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap_array[i] < self.heap_array[i//2]:
                self.heap_array[i], self.heap_array[i//2] = self.heap_array[i//2], self.heap_array[i]
            i = i // 2
    def insert(self, val):
        self.heap_array.append(val)
        self.size = self.size + 1
        self.heapify_up(self.size)
        
    #This is where I extract the root, made the last element as the root
    # before I decrement the size by one and then I heapify down by comparing
    # the left and right child so that way the minimum value would trade places
    # with the left child if the right child is bigger than the left child and 
    # vice versa while I check if the left index is greater or equal to the 
    # heap size.
    def heapify_down(self, i):
        while (2*i) <= self.size:
            minVal = self.min_value(i)
            if self.heap_array[i] > self.heap_array[minVal]:
                self.heap_array[i], self.heap_array[minVal] = self.heap_array[minVal], self.heap_array[i]
            i = minVal
    def min_value(self, i):
        if (2*i)+1 > self.size:
            return 2*i
        else:
            if self.heap_array[2*i] < self.heap_array[(2*i)+1]:
                return 2*i
            else:
                return (2*i) + 1
    def extract_min(self):
        self.heap_array[1] = self.heap_array[self.size]
        self.size = self.size - 1
        self.heap_array.pop()
        self.heapify_down(1)
        
    #This where I made the heap size to equal zero to indicate that the heap 
    # array is empty    
    def is_empty(self):
        return self.size == 0
    
    #This is where I print out the heap array
    def printHeap(self):
        for i in range(1, len(self.heap_array)):
            print(self.heap_array[i])
            
#This is where I display my results
h = Heap()
print("Insert:")
h.insert(3)
h.insert(7)
h.insert(9)
h.insert(5)
h.insert(1)
h.printHeap()
print("Extract Min:")
h.extract_min()
h.printHeap()
print("To Check If It Is Empty:")
print(h.is_empty())
            
        
