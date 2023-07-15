#numpy array
import numpy as np
arr=np.array([[1,2,3],
             [4,2,5]])
print("Array is of type: ",type(arr))
print("Number of dimentions: ",arr.ndim)
print("Shape of array: ",arr.shape)
print("Size of array: ",arr.size)
print("Array stroes element of type:",arr.dtype)

#linaer algebra in numpy
import numpy as np
x=np.array([[1,2],
               [3,4]])
y=np.array([[5,6],
               [7,8]])
print("The element wise addition of matrix: ")
print("Addition: ", np.add(x,y))
print("Subtraction: ", np.subtract(x,y))
print("Division: ", np.divide(x,y))
print("Multiplication: ",np.multiply(x,y))

#image in numpy
import cv2
import numpy as np
array_created=np.full((500,120, 8)),
(255,dtype=np.uint8)
cv2.imshow("image",array_created)