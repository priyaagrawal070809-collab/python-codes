import time
import tracemalloc
#harshad number is that whose sum is divisor of the number(1+8=9,18//9=2, hence no reminder)
def is_harshad(n):
    original = n
    digit_sum = 0
    while n != 0:
        digit = n % 10
        digit_sum += digit
        n = n // 10
    return original % digit_sum == 0

n= int(input("Enter a number:"))

tracemalloc.start()
start = time.time()

result = is_harshad(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Is Harshad:", result)
print("Runtime: {:.8f} seconds".format(end - start))
print("Peak Memory Usage: {:.8f} MB".format(peak / 10**6))
