def sumofevennumbers(m, n):
    sum_even = 0
    for num in range(m, n + 1):
        if num % 2 == 0:  
            sum_even += num
    return sum_even
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    m, n = map(int, input("Enter m and n separated by a space: ").split())
    result = sumofevennumbers(m, n)
    print("Sum of even numbers from", m, "to", n, "is:", result)
