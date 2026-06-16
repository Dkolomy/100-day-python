def fizz_buzz(target):
    for number in range(1, target + 1):
        # The problem is the logic in the first 'if' condition.
        # It checks 'number % 3 == 0 or number % 5 == 0', meaning
        # any number divisible by 3 or 5 will print "FizzBuzz".
        # This prevents the program from ever printing "Fizz" or "Buzz"
        # on their own, and even prints "FizzBuzz" for values that are only divisible by 3 or only by 5.
        # The correct logic should check if the number is divisible by both 3 and 5 (using 'and'),
        # then check for 3 and 5 individually.
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
 
