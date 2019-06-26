#                11. Euclidean distance
x1 = int(input("Enter Co-ordinate for x1:"))
y1 = int(input("Enter Co-ordinate for y1:"))
x2 = int(input("Enter Co-ordinate for x2:"))
y2 = int(input("Enter Co-ordinate for y2:"))
distance =((x2-x1)**2+(y2-y1)**2)**(1/2)
print("Distance between points(",x1,",",y1,") and (",x2,",",y2,") is ",distance)