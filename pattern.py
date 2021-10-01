 
k = (2 * 3) - 2  
for i in range(4, -1, -1):  
    # Inner loop will print the number of space.  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    # This inner loop will print the number o stars  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  
m = (2 * 5) - 2
for i in range(0, 5):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("*", end=' ')  
    print(" ")  