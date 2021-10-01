for num in range(100 ,1000):
    #num=1234
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10
    add=num+reverse
   
    print(add)
