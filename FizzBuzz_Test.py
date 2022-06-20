# Write a fizzbuzz function that returns a vector<string> with the numbers from 1 to n with the following restrictions:

# for multiples of 3 store "Fizz" instead of the number

# for multiples of 5 store "Buzz" instead of the number

# for numbers which are multiples of both 3 and 5 store "FizzBuzz"

# You may use the std::to_string(number) method to convert a number into a string

n = 10
def fizzbuzz(n):
    t = []
    for i in range(1,n+1):
        if i%3 == 0:t.append("Fizz")
        elif i%5 == 0:t.append("Buzz")
        elif i%3 and i%5 == 0:t.append("FizzBuzz")
        else:t.append(i)
    return t

print(fizzbuzz(n))