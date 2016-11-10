def bubblesort():
	unsorted = [1,90,343,54,11,43,23,76,54,93,3,01,10]
	for i in range( len( unsorted ) ):
		for k in range( len( unsorted ) - 1, i, -1 ):
			if(unsorted[k]<unsorted[i]):
				unsorted[k], unsorted[i] = unsorted[i], unsorted[k] 
				"""temp = unsorted[k]
				unsorted[k]=unsorted[i]
				unsorted[i]=temp"""

	print unsorted

def insertionsort():
	unsorted = [1,90,343,54,11,43,23,76,54,93,3,01,10]
	for i in range(len(unsorted)):
		for k in range(len(unsorted[:i])):
			if(unsorted[i]<unsorted[k]):
				unsorted[k], unsorted[i] = unsorted[i], unsorted[k] 
	print unsorted

bubblesort()
insertionsort()
