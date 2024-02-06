fh =open('output.txt','w')
length = int(input("Enter the length of Rectangle : "))
breath = int(input("Enter the breath of Rectangle : "))

Area = length * breath
Perameter = 2 * (length + breath)

fh.write("Area of Rectangle is :" + str(Area)+'\n')
fh.write("Perimeter of Rectangle is :" + str(Perameter) + '\n')
fh.close