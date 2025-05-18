def fibonacci(n):
    if n <= 0:   # F(0) = 0
        return 0
    elif n == 1:  # F(1) = 1
        return 1
    else:  # F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(4) #3

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("amin")) #nima
