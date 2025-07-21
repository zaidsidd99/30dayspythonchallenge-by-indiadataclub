# def remote_control_next():
#     yield "cnn"
#     yield "espn"

# for c in remote_control_next():\
# print (c)



# def fib ():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# for f in fib ():
#     if f> 50:
#         break
#     print(f)


# Generate the first n Fibonacci numbers with a generator ?

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 10
for num in fibonacci_generator(n):
    print(num)
