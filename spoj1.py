while True:
    try:
        num = int(input("Enter a number :"))
        if num == 42:
            break 
        print(num)  
    except ValueError:
        print("Invalid")
