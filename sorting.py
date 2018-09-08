# -*- coding: utf-8 -*-
import unittest 

class Sort():
	"""
	Implement two method to sort a list : QuickSort and MergeSort. --> Readme for the complexity analysis
	"""

	@staticmethod
	def quickSort(arr,start,end):
		"""
			Implementation of the quicksort algorithm

			:param arr: Array to sort
			:param start: Leftmark (next element after the pivot)
			:param end: Rightmark
			:type arr: obj<list>
			:type start:int
			:type end:int

			:return: None
		"""
		if start < end:	
			pIndex = Sort._partition(arr,start,end)
			Sort.quickSort(arr,start,pIndex-1)
			Sort.quickSort(arr,pIndex + 1,end)

	@staticmethod
	def _partition(arr,start,end):
		"""
		Pick a pivot value and rearange the values in the list in order than values lower than pivot are placed on the left 
		and values higher than pivot are placed on the right

		:param arr: Array to sort
		:param start: Leftmark (next element after the pivot)
		:param end: Rightmark
		:type arr: obj<list>
		:type start:int
		:type end:int

		:return: The index of the pivot
		:rtype: int 
		"""

		pivot = arr[start]
		done = False

		leftcur = start + 1
		rightcur = end

		while not done:
			while arr[leftcur] <= pivot and leftcur <= rightcur:
				leftcur += 1
			while arr[rightcur] >= pivot and rightcur >= leftcur:
				rightcur -= 1
			if rightcur < leftcur:
				done = True
			else:
				arr[leftcur], arr[rightcur] = arr[rightcur], arr[leftcur]

		arr[start],arr[rightcur] = arr[rightcur], arr[start]	
		return rightcur

	@staticmethod
	def mergeSort(arr):
		"""
		Implementation of the mergeSort algorithm. Divide successively a list into 2 parts until the base case when length 
		of the list is 1. Then merge the sorted list

		:param arr: Array to sort
		:type arr: obj<list>

		:return: None
		"""
		n = len(arr)
		if n > 1:
			mid = n//2
			left = arr[:mid]
			right = arr[mid:]

			Sort.mergeSort(left)
			Sort.mergeSort(right)

			i = 0
			j = 0
			k = 0

			while i < len(left) and j < len(right):
				if left[i] < right[j]:
					arr[k] = left[i]
					i += 1
				else:
					arr[k] = right[j]
					j += 1
				k += 1

			while i < len(left):
				arr[k]=left[i]
				i+=1
				k+=1

			while j < len(right):
				arr[k] = right[j]
				j+=1
				k+=1

class TestSort(unittest.TestCase):

	def testQuickSort(self):
		arr1 = [54,26,93,17,77,31,44,55,32]
		Sort.quickSort(arr1,0,len(arr1)-1)
		print("sorted : ",arr1)
		self.assertTrue(arr1 == [17,26,31,32,44,54,55,77,93])

	def testMergeSort(self):
		arr1 = [54,26,93,17,77,31,44,55,32]
		Sort.mergeSort(arr1)
		self.assertTrue(arr1 == [17,26,31,32,44,54,55,77,93])

if __name__ == "__main__":
		unittest.main()	









