def Rectangle(width, height):
  #calculate the area
  Area = width * height
  #calculate the perimeter
  Perimeter = 2 * (width + height)
  print("\n Area of the Rectangle is: %.2f" %Area)
  print("\n Perimeter of the Rectangle is: %.2f" %Perimeter)
width = float(input("Enter the Width of Rectangle: "))
height = float(input("Enter the Height of Rectangle: "))
Rectangle(width, height)
