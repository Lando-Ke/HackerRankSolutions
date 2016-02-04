#Given a sorted array (ar) and a number (V), can you print the 
#index location of V in the array?

v= 4

ar= [1, 4, 5, 7, 9, 12]

print len(ar)


for i in xrange(len(ar)):
	if ar[i]==v:
		print i