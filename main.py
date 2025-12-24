def square(n):
    iter = 0
    for i  in range(0,n):
        for j in range(0,n):
            print("$", end= " " )
            iter += 1
        print("")
square(6) 
print("16")
square(16)
