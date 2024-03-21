x=int(input("Enter the number you want to multiply:"))
y=int(input("Enter the multiplication limit:"))
for i in range(x,x+2):
    for j in range (1,y+1):
        w=i*j
        print(f"{i}x{j}={w}")

