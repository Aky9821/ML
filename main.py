import numpy as np

a= np.array([[1,2],[3,4],[5,6]])


#print(a.shape)

a.resize(6,1)

b=np.arange(0,20,0.5)
#print(a)
#print(b)
#print(ndim)

c=np.ones([5,4])
#print(c)

a=np.array([[0,1,2],[2,3,4]])
b=np.array([1,2,3])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.dot(a,b))

print(np.amin(a,axis=0))
print(np.amax(a,axis=0))

print(np.amin(a,axis=1))
print(np.amax(a,axis=1))

print(np.ptp(a))

print(np.ptp(a,axis=0))
print(np.ptp(a,axis=1))

print(np.median(a))
print(np.mean(a))
print(np.average(a))

print(np.std(a))
print(np.var(a))
print(a.shape);
#a.resize(3,3);
print(a);

a=np.arange(1,20,2).reshape(2,5);
b=np.arange(20,40,2).reshape(5,2);
print(a);
print(b);
b.resize(2,5);
print(np.add(a,b));

print(np.median(a))
print(np.mean,axis=1)
print(np.average, axis=0)