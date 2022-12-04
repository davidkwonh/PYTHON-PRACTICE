#   If and Else statement practice

#   Day 231 of the job hunt. At this point I have embraced the recession fully. Who knows when I will get a job. I am sitting at 7leaves desperately wishing for my coffee to be stronger.

#   FIZZBUZZ
for n in range(1,101):
    if n % 15 ==0:
        print("FIZZBUZZ")
    else:
        if n % 3 == 0:
            print("FIZZ")
        else:
            if n % 5 == 0:
                print("BUZZ")
            else:
                print(n)

#   Cleaner Code

for n in range(1,101):
    if n % 15 ==0:
        print("FIZZBUZZ")
    elif n % 3 == 0:
        print("FIZZ")
    elif n % 5 == 0:
        print("BUZZ")
    if n%2==0:
        print("EVEN")

# Ternary operator: takes in a bool condition and evaluates it and returns a value based upon T or F
fizzbuzz = "Fizzbuzz" if n%15==0 else "Fizz" if n%3==0 else "Buzz" if n%5==0 else n

simplify = ["Fizzbuzz" if n%15==0 else "Fizz" if n%3==0 else "Buzz" if n%5==0 else n for n in range (1,101)]
print(simplify)


