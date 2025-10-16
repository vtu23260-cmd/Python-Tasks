task 8.a

def number_sequence(start, end, step=1):
    current = start
    while current <= end:
        yield current
        current += step
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step value: "))
# Create the generator
sequence_generator = number_sequence(start, end, step)
# Print the generated sequence of numbers
for number in sequence_generator:
    print(number)

    task 8.b
    
    def prime_generator(n):
    # Generate prime numbers up to n
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# Take user input
n = int(input("Enter the upper limit to generate primes: "))

# Create the generator
prime_gen = prime_generator(n)

# Print the generated prime numbers
print(f"Prime numbers up to {n}:")
for p in prime_gen:
    print(p)

    
    task 8.c
    
    
    def log_prime(func):
    def wrapper(n):
        for prime in func(n):
            print(f"Prime generated: {prime}")  # log each prime
            yield prime
    return wrapper

@log_prime
def prime_generator(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            yield num

# Generate primes up to 20
for p in prime_generator(20):
    pass

  
  task 8.d
  
  def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

def lowercase_decorator(func):
    def wrapper(text):
        return func(text).lower()
    return wrapper

@uppercase_decorator
def shout(text):
    return text

@lowercase_decorator
def whisper(text):
    return text

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)
