import numpy as np

a = np.array([1,2,4,5], float) #creating arrays
print 'the array is',a
print 'the type of a is',type(a)
print 'values of a upto 1: ', a[:2]
a[0] = 5
print 'changed a[0] to 5: ',a
b = np.array([[6,7,4,9], [45,78,35,56]], float)
print 'values of multi dimensional array ', b
print 'b [0] values ', b[0]
print 'b[0,0] value ', b[0,0]
print 'b[0,1] value ', b[0,1]
print 'b[1, :] is everything in second array ', b[1, :]
print 'b[:, 2] in all rows elem at index 2 ', b[:, 2]
print 'b[-1:, -2:] ie last row all elems econd from last index ', b[-1:,-2:]
print 'b.shape ', b.shape
print 'len(a) shows the length of first axis ', len(a)
print 'test in ', 2 in b
c = b.reshape((4,2))
print 'new shape of b 4 cols of 2 elems: ', c
print c.shape
print b
e = b
d = e.copy()
print 'e = b new e ', e
e[0,0] = 89
print b
print 'd = a.copy() ', d
print 'e[0, 0] = 89 ', e
print b
print list(a)
print b.transpose()
print a.flatten()
f = np.eye(4, k=1, dtype=float)
print f




























