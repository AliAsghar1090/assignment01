from PIL import Image
import numpy
num_array=[]
y=0
while y<20:
    y=y+1
    num_array.append(y)

array = []
for num in num_array:
   im = Image.open("image"+str(num)+".jpg")
   np_im = numpy.array(im)
   array.append("image"+str(num)+".jpg")
   array.append(np_im)
#print(num_array)
print(array)

